from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 30
    max_page_size = 50
    page_size_query_param = 'limit'
    page_query_param  = 'page'
    last_page_strings = ('last', 'end')

    def get_paginated_response(self, data):
        return Response({
            'status': "Success",
            'count': self.page.paginator.count,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'data': data
        })
    