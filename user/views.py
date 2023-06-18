from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupFrom
from user.models import User

def signUp(request):
    if request.method=='POST':
        form=SignupFrom(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['first_name']
            lname=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            contact=form.cleaned_data['contact']
            password=form.cleaned_data['password']
            user=User(first_name=fname,last_name=lname,email=email,contact=contact,password=password)
            user.save()
            return HttpResponse("thank you")
        else:
            return HttpResponse("EnterValidData")
            
    form=SignupFrom()
    return render(request,"user/signup.html",{"form":form})
