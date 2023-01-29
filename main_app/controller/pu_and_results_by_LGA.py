from operator import itemgetter 
from utils.utils import Request, Response
from exceptions.marshmallow_exceptions import WrongFieldType
from main_app.schemas import pu_and_results_schema
from main_app.pagination.paginator import CustomPagination
from main_app.repositories.polling_unit_repo import PollingUnitsRepo
from main_app.repositories.polling_unit_results_repo import PollingUnitResultsRepo
from main_app.serializers.pu_and_results_serializer import PUAndResultsSerializer


class PollingUnitsAndResultsByLGAController:
    def __init__(self) -> None:
        self.request = Request
        self.response = Response()
        self.pu_repo = PollingUnitsRepo()
        self.pu_results_repo = PollingUnitResultsRepo()
        self.paginator = CustomPagination()
        self.serializer = PUAndResultsSerializer
        self.schema = pu_and_results_schema

    def get_pu_and_results_by_LGA(self, polling_unit) -> tuple:
        pu_results_query_set = self.pu_results_repo.filter_by_keyword(polling_unit.uniqueid, "polling_unit_uniqueid")
        return {
            'polling_unit': polling_unit,
            'polling_unit_results': pu_results_query_set
            }

    def get_pu_and_results_by_LGA_response(self, request):
        id, = Request(request).required('lga-id')
                
        polling_units_query_set = self.pu_repo.filter_by_keyword(id, 'lga_id')
        pu_and_results = list(
            map(
                lambda i: self.get_pu_and_results_by_LGA(i),
                polling_units_query_set
            ))
        paginated_query_set = self.paginator.paginate_queryset(pu_and_results, request)
        data = self.serializer(paginated_query_set, many=True).data
        self = self.paginator.get_paginated_response(data)

        return self

    def create_pu_and_results_by_LGA_response(self, request):
        try:
            pu_and_results = self.schema.PUandResultsSchema().load(request.data)
        except Exception as e:
            raise WrongFieldType(e)

        polling_unit = itemgetter('polling_unit')(pu_and_results)
        polling_unit_obj = self.pu_repo.create(**polling_unit)

        def change_key_value(obj: dict, key: str, value):
            obj[key] = value
            return obj

        polling_unit_results = itemgetter('polling_unit_results')(pu_and_results)
        polling_unit_results = list(
            map(
                lambda i: change_key_value(i, 'polling_unit_uniqueid', polling_unit_obj.uniqueid), 
                polling_unit_results
            ))
        polling_unit_result_objs = self.pu_results_repo.bulk_create(*polling_unit_results)

        data = {
            'polling_unit': polling_unit_obj,
            'polling_unit_results': polling_unit_result_objs
        }
        payload = self.serializer(data).data
        self = self.response.data_response(payload)
        
        return self
