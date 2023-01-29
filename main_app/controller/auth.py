from datetime import timedelta, datetime
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from django.conf import settings
from rest_framework.exceptions import NotFound
from main_app.models import Code
from exceptions.jwt_exceptions import InvalidToken, TokenExpired
from utils.utils import Request, Response


class AuthController:
    def __init__(self) -> None:
        self.jwt = jwt
        self.model = Code
        self.request = Request
        self.response = Response()

    def check_code(self, code: None | str = None):
        if code is None:
            code = self.code
        try:
            code = self.model.objects.get(code=code)
        except self.model.DoesNotExist:
            raise NotFound("You supplied an invalid code")
        self.code_obj = code
        return self

    def gen_token_from_code(self, code: None | str = None, exp_time=8):
        if code is None:
            code = self.code_obj.code
        payload = {
            "ID": code,
            "exp": datetime.utcnow() + timedelta(hours=exp_time)
        }
        token = self.jwt.encode(
            payload=payload,
            key=settings.SECRET_KEY,
            algorithm=settings.CRYPTOGRAPHIC_ALGORITHM
        )
        self.token = token
        return self

    def get_code_from_token(self, token: None | str = None):
        if token is None:
            token = self.token
        try:
            payload = self.jwt.decode(
                token,
                key=settings.SECRET_KEY,
                algorithms=[settings.CRYPTOGRAPHIC_ALGORITHM]
                )
        except ExpiredSignatureError:
            raise TokenExpired
        except InvalidTokenError:
            raise InvalidToken
        self.code = payload.get("ID")
        return self

    def get_access_token_response(self, request):
        access_code, = Request(
            request, method="POST"
            ).required("accessCode", error_message="Access Code is required")
        token = self.check_code(access_code).gen_token_from_code()
        payload = {
            "accessToken": token.token
        }
        self = self.response.data_response(payload)
        return self
        