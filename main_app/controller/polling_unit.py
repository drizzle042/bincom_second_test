from utils.utils import Request, Response
from main_app.pagination.paginator import CustomPagination
from main_app.repositories.polling_unit_repo import PollingUnitsRepo
from main_app.serializers.polling_unit_serializer import PollingUnitSerializer


class PollingUnitsController:
    def __init__(self) -> None:
        self.request = Request
        self.response = Response()
        self.repo = PollingUnitsRepo()
        self.paginator = CustomPagination()
        self.serializer = PollingUnitSerializer

    def get_polling_units_response(self, request):
        id, keyword = Request(request).opts("id", "keyword")
        if id:
            query_set = self.repo.get_by_keyword("uniqueid", id)
            data = self.serializer(query_set).data
            self = self.response.data_response(data)
        elif keyword:
            query_set = self.repo.filter_by_keyword(keyword, *self.repo.filter_fields)
            paginated_query_set = self.paginator.paginate_queryset(query_set, request)
            data = self.serializer(paginated_query_set, many=True).data
            self = self.paginator.get_paginated_response(data)
        else:
            query_set = self.repo.all().order_by("-date_entered")
            paginated_query_set = self.paginator.paginate_queryset(query_set, request)
            data = self.serializer(paginated_query_set, many=True).data
            self = self.paginator.get_paginated_response(data)

        return self
