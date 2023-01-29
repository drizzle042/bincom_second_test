from rest_framework.views import exception_handler


def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)
    response.data['status'] = "Error"
    response.data['message'] = response.data.pop('detail')

    return response