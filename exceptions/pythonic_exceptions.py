from rest_framework.exceptions import APIException

class FieldRequired(APIException):
    status_code = 400
    default_detail = 'Missing Field Required'
    default_code = 'bad request'
