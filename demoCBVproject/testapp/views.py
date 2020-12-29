from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>this is response from demo programme</h1>')
class HelloWorldTemplatesView(TemplateView):
    template_name='testapp/result.html'
