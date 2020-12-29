from django.shortcuts import render
from testapp.forms import AddItems
# Create your views here.
def add_items(request):
    form=AddItems()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        

    return render(request,'testapp/form.html',{'form':form})

def display_items(request):
    return render(request,'testapp/display.html')

def del_session(request):
    request.session.modified=True
    for key in request.session.keys():
        del request.session[key]
    return add_items(request)
