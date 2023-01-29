from rest_framework.exceptions import APIException

class WrongFieldType(APIException):
    status_code = 400
    default_detail = 'Wrong field type provided'
    default_code = 'bad request'