from django.shortcuts import render,HttpResponse,redirect
from appnew.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

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

def handlesignup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)>10:
            messages.error(request,"username must be under 10 caharacter")
            return redirect('/')

        
        if not username.isalnum():
            messages.error(request,"username must have alpha  numeric")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request,"password do not match")
            return redirect('/')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"Successfully Created ")
        return redirect('/')

    else:
        return HttpResponse('404 not found')

def handlelogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,'Successfully Loged In!')
            return redirect('/')
        else:
            messages.warning(request,"Invalid Creds!Please Try Again")
            return redirect('/')
        
    return HttpResponse('404 - not found')

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')

    return HttpResponse('handlelogout')
