
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('this will be executed before calling')
        response = self.get_response(request)
        print('this will be executed after calling')
        return response

from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        return HttpResponse('<h1>wesite under maintenance</h1>')
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        s1='<h1>currently we are facing some technical problem</h1> <hr> '
        s2='<h1>Raised Exception:{}</h1>'.format(exception.__class__.__name__)
        s3='<h1>message:{}</h1>'.format(exception)
        return HttpResponse(s1+s2+s3)




class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('this will be executed before  first calling')
        response = self.get_response(request)
        print('this will be executed after first calling')
        return response

class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('this will be executed before second calling')
        response = self.get_response(request)
        print('this will be executed after second calling')
        return response

class ThirdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('this will be executed before  third calling')
        response = self.get_response(request)
        print('this will be executed after third calling')
        return response
