#28.02.24
from django.shortcuts import redirect

class GlobalExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            print("ererere")
            return redirect('error')

        return response
