from typing import Any
from django import forms
from account.models import User


class UserUpdateForm(forms.ModelForm):
   username = forms.CharField(
      label="",
      required=True,
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "form-control",
            "id": "username",
            "type": "text",
            "style":"margin-left: 0px !important; min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      ),
   )

   email = forms.EmailField(
      label="",
      required=True,
      widget=forms.EmailInput(
         attrs={
            "placeholder": "example@email.com",
            "class": "form-control",
            "id": "email",
            "type": "email",
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      ),
   )

   profile_picture = forms.ImageField(
      label="",
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "accept": "image/*",
            "class": "form-control",
            "id": "profile_picture",
            "onchange":"loadFile(event)",
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      ),
   )

   background_image = forms.ImageField(
      label="",
      required=False,
      widget=forms.FileInput(
         attrs={
            "type": "file",
            "placeholder": "",
            "accept": "image/*",
            "class": "form-control",
            "id": "user_login",
            "onchange":"loadBgFile(event)",
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      ),
   )

   first_name = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Firstname",
            "class": "form-control",
            "id": "first_name",
            "type": "text",
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      )
   )

   last_name = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
      attrs={
         "placeholder": "Lastname",
         "class": "form-control",
         "id": "last_name",
         "type": "text",
         "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
      }
      )
   )

   mobile_no = forms.CharField(
      label='',
      max_length=14,
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "+234...",             
            "class": "form-control",
            "id": "mobile_no",
            "maxlength": 14,
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      )
   )   


   bio = forms.CharField(
      label='',
      required=False,
      widget=forms.Textarea(
         attrs={
            "placeholder": "Brief description for your profile.",
            "class": "form-control",
            "id": "bio",
            "type":"textarea",
            "style":"width: 100%;  padding: 0 18px; border:none; resize: none",
            "cols": "55",
            "rows": "5",
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      )
   )

   address = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "3 Saka Street, Lagos, Nigeria",
         "class": "form-control",
         "id": "address",
         "type": "text",
         "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
      }
      )
   )

   date_of_birth = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "form-control profileDate bg-white",
            "placeholder":"Date of Birth",
            "id": 'date_of_birth',
            "style":"margin-left: 0px !important;min-height:42px !important;line-height: 42px;padding: 0 18px !important;background: 0 0;border: 1px solid #eee;color: #959697;"
         }
      )
   )

   gender_choices =  [
      ('Male', 'Male'),
      ('Female', 'Female'),
      ('Other', 'Other'),
      ('not_saying', 'Prefer not to say'),
   ]

   gender = forms.CharField(
      label='',
      required=False,      
      widget=forms.RadioSelect(
         choices=gender_choices,
         attrs={
            'class': 'form-check-input',
            'id': 'gender',
            "style":"margin-left: 0px !important"
         }
      )
   )

   class Meta:
      model = User
      fields = (
         "username",
         "first_name",
         "last_name",
         "email",
         "profile_picture",
         "background_image",
         "bio",
         "address",
         "mobile_no",
         "date_of_birth",
         "gender",                  
      )

      def __init__(self, *args: Any, **kwargs: Any) -> None:
         super(UserUpdateForm, self).__init__(*args, **kwargs)

         for fieldname in (
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "background_image",
            "bio",
            "address",
            "mobile_no",
            "date_of_birth",
            "gender",  
         ):
            self.fields[fieldname].help_text = None

