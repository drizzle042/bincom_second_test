from utils.utils import Request, Response
from main_app.pagination.paginator import CustomPagination
from main_app.repositories.polling_unit_results_repo import PollingUnitResultsRepo
from main_app.serializers.polling_unit_result_serializer import PollingUnitResultSerializer


class PollingUnitResultController:
    def __init__(self) -> None:
        self.request = Request
        self.response = Response()
        self.repo = PollingUnitResultsRepo()
        self.paginator = CustomPagination()
        self.serializer = PollingUnitResultSerializer

    def get_polling_unit_results_response(self, request):
        id, keyword, polling_unit_id = Request(request).opts("id", "keyword", "polling-unit-id")
        if id:
            query_set = self.repo.get_by_keyword("result_id", id)
            data = self.serializer(query_set).data
            self = self.response.data_response(data)
        elif keyword:
            query_set = self.repo.filter_by_keyword(keyword, *self.repo.filter_fields)
            paginated_query_set = self.paginator.paginate_queryset(query_set, request)
            data = self.serializer(paginated_query_set, many=True).data
            self = self.paginator.get_paginated_response(data)
        elif polling_unit_id:
            query_set = self.repo.filter_by_keyword(polling_unit_id, "polling_unit_uniqueid")
            paginated_query_set = self.paginator.paginate_queryset(query_set, request)
            data = self.serializer(paginated_query_set, many=True).data
            self = self.paginator.get_paginated_response(data)
        else:
            query_set = self.repo.all().order_by("-date_entered")
            paginated_query_set = self.paginator.paginate_queryset(query_set, request)
            data = self.serializer(paginated_query_set, many=True).data
            self = self.paginator.get_paginated_response(data)

        return self
