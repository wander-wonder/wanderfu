from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, AddForm
from .models import img


# Create your views here.
def showxiaoxin(request):
    return render(request, 'account/showxiaoxin.html')


def add(request):
    if request.method == "POST":
        af = AddForm(request.POST, request.FILES)
        if af.is_valid():
            name = af.cleaned_data['name']
            headimg = af.cleaned_data['headimg']
            user = img(name=name, headimg=headimg)
            user.save()
            return render(request, 'account/index.html',context={"user":user})
    else:
        af = AddForm()
        return render(request, 'account/add.html',context={"af":af})

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Wellcome You. You have been authenticated successfully.")
            else:
                return HttpResponse("Sorry, Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form":login_form})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, you can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form":user_form, "profile":userprofile_form})