from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.core.validators import validate_email

from account.models import User


class UserSignUpForm(UserCreationForm):
    email = forms.CharField(label='Email', max_length=50)
    username = forms.CharField(label='username', max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = User
        
    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #     if password and password2 and password != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user = User.objects.create_user(
                    username=self.cleaned_data["username"],
                    email=self.cleaned_data["email"],
                    password=self.cleaned_data["password1"],
                )
        user.is_staff = True
        if commit:
            user.save()
        return user

# class CreatorSignUpForm(UserCreationForm):
#     email = forms.CharField(label='Email', max_length=50)
#     username = forms.CharField(label='username', max_length=50)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fiields = ('email','username','password1', 'password2')
        
#     # def clean_username(self):
#     #     username = self.cleaned_data['username']
#     #     if User.objects.filter(username=username).exists():
#     #         raise forms.ValidationError("Username has been taken")
        
#     # def clean_password2(self):
#     #     # Check that the two password entries match
#     #     password1 = self.cleaned_data.get("password1")
#     #     password2 = self.cleaned_data.get("password2")
#     #     if password1 and password2 and password1 != password2:
#     #         raise forms.ValidationError("Passwords don't match")
#     #     return password2
    

#     # def clean_email(self):
#     #     email = self.cleaned_data["email"]
#     #     if User.objects.filter(email=email).exists():
#     #         raise forms.ValidationError("Email address has already been used!")

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user = User.objects.create_user(
#                     username=self.cleaned_data["username"],
#                     email=self.cleaned_data["email"],
#                     password=self.cleaned_data["password1"],
#                 )
#         # user.set_password(self.cleaned_data["password1"])
#         user.is_staff = True
#         if commit:
#             user.save()
#         return user
    