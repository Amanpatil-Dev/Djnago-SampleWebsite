from django.shortcuts import render,HttpResponse
from appnew.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'About.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Thanks For The FeedBack !')
    return render(request,'contact.html')