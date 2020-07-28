from django.shortcuts import render
from . import forms
from . import models
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def about(request):
    return render(request,"wallet/about.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('wallet:about'))


def user_login(request):
    invalid_user = False
    acc_not_active = False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('wallet:dashboard'))
            else:
                acc_not_active = True
                return render(request,"wallet/login.html",{'invalid_user':invalid_user,'acc_not_active':acc_not_active})
        else:
            print("Invalid User")
            print("Username: {} and password {}".format(username,password))
            invalid_user = True
            return render(request,'wallet/login.html',{'invalid_user':invalid_user,'acc_not_active':acc_not_active})
    else:
        return render(request,"wallet/login.html",{'invalid_user':invalid_user,'acc_not_active':acc_not_active})



def register(request):
    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user =  user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileForm()

    return render(request,"wallet/register.html",{"user_form":user_form,"profile_form":profile_form,'registered':registered})




@login_required
def dashboard(request):
    # balance = models.balance.objects.all()

    return render(request,"wallet/dashboard.html")
