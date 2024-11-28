from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Login
#password for test is Abhay@1234
# Create your views here.
def index(request):
    context={
        "variable" : "this is sent"   
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is homepage')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('this is about page')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is services page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')
    #return HttpResponse('this is contact page')

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        login = Login(name = name, email = email, phone = phone, date = datetime.today())
        login.save()
    return render(request, 'login.html')
    #return HttpResponse('this is page')
