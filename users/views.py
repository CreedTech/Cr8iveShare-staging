from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from account.models import UserSettings
from .forms import UserUpdateForm
from django.contrib import messages
from account.models import User
from account.views import user_logout



@login_required
def dashboard(request, slug):     
   context = {}
   return render(request, 'users/dashboard.html', context)


@login_required
def user_profile(request, slug):
   # user_object = User.objects.get(username=slug)
   # user_profile = UserSettings.objects.get(user=user_object)
   context = {
      # 'user_object': user_object,
      # 'user_profile': user_profile,
   }
   return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request, slug):
   if request.method == "POST":
      user_form = UserUpdateForm(request.POST or None, request.FILES or None, instance = request.user)

      if user_form.is_valid():
         user_form.save()
         messages.success(request, "Profile updated successfully.")
         return redirect('core:channels_list')
      else:
         messages.error(request, "Enter all correct details.")
         return redirect(request.META.get("HTTP_REFERER"))
   else:
      user_form = UserUpdateForm(instance=request.user)

   context = {
      'user_form': user_form,
   }   
   return render(request, 'users/edit_profile.html', context)

@login_required
def delete_account(request, slug):
   user = User.objects.get(slug=slug)
   user.is_active = False
   user.save()
   messages.success(request, "Account deleted successfully! 👋")
   return redirect('/')


def author_external(request, slug):   
   author = User.objects.get(slug=slug)
   if request.user == author:
      return redirect('users:profile', slug=slug)   
   else:
      context = {
         'author': author
      }
      return render(request, 'users/author-external.html', context)
   