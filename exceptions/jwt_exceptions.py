from rest_framework.exceptions import APIException

class TokenExpired(APIException):
    status_code = 401
    default_detail = 'Your token has expired.'
    default_code = 'token expired'


class InvalidToken(APIException):
    status_code = 401
    default_detail = 'Your token is invalid.'
    default_code = 'token inalid'