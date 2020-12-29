from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'newsapp/home.html')
def movienews(request):
    heading='this is movies news heading'
    data1='this is movies news heading 1'
    data2='this is movies news heading 2'
    data3='this is movies news heading 3'
    my_dict={'heading':heading,'data1':data1,'data2':data2,'data3':data3}
    return render(request,'newsapp/news.html',context=my_dict)
def sportsnews(request):
    heading='this is sports news heading'
    data1='this is sports news heading 1'
    data2='this is sports news heading 2'
    data3='this is sports news heading 3'
    my_dict={'heading':heading,'data1':data1,'data2':data2,'data3':data3}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsnews(request):
    heading='this is  politics news heading'
    data1='this is  politics news heading 1'
    data2='this is  politics news heading 2'
    data3='this is  politics news heading 3'
    my_dict={'heading':heading,'data1':data1,'data2':data2,'data3':data3}
    return render(request,'newsapp/news.html',context=my_dict)
