from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['code'] = response.status_code
        if "detail" in response.data:
            response.data['code'] = 201
            if response.data['detail'] == "No active account found with the given credentials":
                response.data['message'] = "用户名或密码错误"
            elif response.data['detail'] == "User is not active":
                response.data['message'] = "当前用户未激活"
                response.data['code'] = 401
            elif response.data['detail'] == "Invalid token.":
                response.data['message'] = "token无效"
                response.data['code'] = 401
            elif response.data['detail'] == "Authentication credentials were not provided.":
                response.data['message'] = "未提供认证信息"
                response.data['code'] = 401
            elif response.data['detail'] == "Given token not valid for any token type":
                response.data['message'] = "token无效"
                response.data['code'] = 401
            else:
                response.data['message'] = response.data['detail']
        response.status_code = 200
        response.data.pop('detail', None)

    return response