from django.http import JsonResponse
import jwt
import os
from django.core.cache import cache

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_authorized, data = self.is_authorized(request)
        
        if not is_authorized:
            return JsonResponse({
                "status": 401,
                "messages": ["failed.unauthorize"],
                "data": None,
                "toast": True
            }, status=401)

        request.header = data

        response = self.get_response(request)
        return response

    def is_authorized(self, request):
        excluded_paths = ['/api/auth/login/', '/api/auth/login', '/apis/', '/apis']
        try:
            if request.path in excluded_paths:
                return True, None

            auth_header = request.headers.get('Authorization')
            if auth_header:
                result = jwt.decode(auth_header, os.getenv("ACCESS_TOKEN_KEY"), algorithms='HS256')

                access_token = cache.get(result["data"]["access_key"])

                data = dict()
                data['token_decode'] = result
                if access_token is not None:
                    return True, data

            return False, None
        except jwt.ExpiredSignatureError:
            return False, None
        except jwt.DecodeError:
            return False, None
        except Exception as e:
            return False, None