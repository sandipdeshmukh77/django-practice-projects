from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=int(request.COOKIES.get('count',0))
    new_count=count+1
    response=render(request,'testapp/cookies.html',{'count':new_count})
    response.set_cookie('count',new_count)
    return response
