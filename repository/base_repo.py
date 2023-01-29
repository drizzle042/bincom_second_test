from django.db.models import Model, Q
from rest_framework.exceptions import NotFound


class BaseRepo:
    def __init__(self) -> None:
        self.model = Model

    def resolve_lookup_fields(self, keyword, *fields):
        """Takes a tuple of lookup fields and returns a query expression"""
        Qr = None
        for field in fields:
            q = Q(**{f"{field}__icontains": keyword })
            if Qr:
                Qr = Qr | q # or & for filtering
            else:
                Qr = q
        return Qr


    def get_by_keyword(self, field, keyword):
        try:
            query_logic = {field: keyword}
            query_object = self.model.objects.get(**query_logic)
        except self.model.DoesNotExist:
            raise NotFound()
        return query_object

    def filter_by_keyword(self, keyword, *args):
        query_logic = self.resolve_lookup_fields(keyword, *args)
        query_object = self.model.objects.filter(query_logic)
        return query_object

    def all(self):
        query_object = self.model.objects.all()
        return query_object

    def create(self, **kwargs):
        created_obj = self.model.objects.create(**kwargs)
        return created_obj    
        
    def bulk_create(self, *args):
        created_obj = self.model.objects.bulk_create(
            list(map(lambda i: self.model(**i), args)), 
            ignore_conflicts=False)
        return created_obj
        