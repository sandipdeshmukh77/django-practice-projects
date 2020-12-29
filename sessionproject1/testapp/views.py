from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=request.session.get('count',0)
    new_count=count+1
    request.session['count']=new_count
    response=render(request,'testapp/session.html',{'count':new_count})
    return response
