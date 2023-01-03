from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.cache import cache
from django.contrib.auth import authenticate, logout
from account.models import User
from django.contrib import messages
from random_username.generate import generate_username

from account.forms import CreatorSignUpForm, UserSignUpForm


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect("core:index")
    else:
        if request.method == 'GET':
            cache.set('next', request.GET.get('next', None))

        if request.method == "POST":
            username_or_email = request.POST["username_or_email"]
            password = request.POST["password"]

            if User.objects.filter(username=username_or_email).exists():
                username = username_or_email
            elif User.objects.filter(email=username_or_email).exists():
                username = User.objects.get(email=username_or_email).username
            else:
                username = None

            if username is not None:
                # next_page = request.GET['next']
                try:
                    user = authenticate(username=username, password=password)                    
                    auth.login(request, user)
                    messages.success(request, "You are successfully logged in.")                                     
                    # return redirect('users:dashboard', user.slug)   
                    next_url = cache.get('next')
                    if next_url:
                        cache.delete('next')
                        return HttpResponseRedirect(next_url)
                    else:
                        return redirect('users:profile', user.slug)   
                except:
                    messages.error(request, "Incorrect password.")
                    return redirect("login")
            else:
                messages.error(request, "Enter correct details.")
                return redirect("login")
    return render(request, "account/login.html")


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username=request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email address has already been used!")
                    return redirect(request.META.get("HTTP_REFERER")) 
                else:
                    user = form.save()
                    email = form.cleaned_data['email']
                    username=form.cleaned_data['username']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']
                    auth.login(request, user)
                    messages.success(
                        request, 'Account created successfully, please complete your profile'
                    )
                    return redirect('users:edit_profile', user.slug)
            else:
                messages.error(request, "Passwords do not match")
        else:
            messages.error(request, form.errors)
            context = {"form":form }
    else:
        # messages.error(request, "Passwords do not match")
        form = UserSignUpForm()
    context = {
        'form':form
    }
    return render(request, "account/register.html", context)
    # if request.method == "POST":
    #     email = request.POST["email"]
    #     password1 = request.POST["password1"]
    #     confirm_password = request.POST["confirm_password"]

    #     if password1 == confirm_password:
    #         if User.objects.filter(email=email).exists():
    #             messages.error(request, "Email address has already been used!")
    #             return redirect("register")
    #         else:
    #             user = User.objects.create_user(
    #                 username="".join(generate_username()),
    #                 email=email,
    #                 password=password1,
    #             )
    #             auth.login(request, user)
    #             if not user.is_staff:
    #                 messages.success(
    #                     request, 'Account created successfully, please complete your profile'
    #                 )
    #                 return redirect('users:edit_profile', user.slug)
    #     else:
    #         messages.error(request, "Passwords do not match")
    #         return redirect("register")
    # return render(request, "account/register.html")

def creator_register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username=request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        form = CreatorSignUpForm(request.POST)

        if form.is_valid():
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email address has already been used!")
                    return redirect(request.META.get("HTTP_REFERER")) 
                else:
                    user = form.save()
                    email = form.cleaned_data['email']
                    username=form.cleaned_data['username']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']
                    auth.login(request, user)
                    messages.success(
                        request, 'Account created successfully, please create your channel'
                    )
                    return render(request,'channel.html')
            else:
                messages.error(request, "Passwords do not match")
        else:
            messages.error(request, form.errors)
            context = {"form":form }
    else:
        # messages.error(request, "Passwords do not match")
        form = CreatorSignUpForm()
    context = {
        'form':form
    }
    return render(request, "account/register.html", context)


@login_required(login_url='auth/login')
def user_logout(request):
    logout(request)    
    messages.success(request, "See you soon! 👋")
    return redirect(request.META.get("HTTP_REFERER"))    

def forgot_password(request):
    return render(request, 'account/forgot_password.html')