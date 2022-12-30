from typing import Any
from django import forms
from account.models import User, SocialHandle


class UserUpdateForm(forms.ModelForm):
   username = forms.CharField(
      label="",
      required=True,
      widget=forms.TextInput(
         attrs={
            "placeholder": "",
            "class": "input",
            "id": "username",
            "type": "text",
         }
      ),
   )

   email = forms.EmailField(
      label="",
      required=True,
      widget=forms.EmailInput(
         attrs={
            "placeholder": "example@email.com",
            "class": "input",
            "id": "email",
            "type": "email",
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
            "class": "input",
            "id": "profile_picture",
            "onchange":"loadFile(event)"
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
            "class": "input",
            "id": "user_login",
            "onchange":"loadBgFile(event)"
         }
      ),
   )

   first_name = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Firstname",
            "class": "input",
            "id": "first_name",
            "type": "text",
         }
      )
   )

   last_name = forms.CharField(
      label='',
      required=True,
      widget=forms.TextInput(
      attrs={
         "placeholder": "Lastname",
         "class": "input",
         "id": "last_name",
         "type": "text",
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
            "class": "input",
            "id": "mobile_no",
            "maxlength": 14
         }
      )
   )   

   job_title = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "Position at ...",
         "class": "input",
         "id": "job_title",
         "type": "text",
      }
      )
   )

   bio = forms.CharField(
      label='',
      required=False,
      widget=forms.Textarea(
         attrs={
            "placeholder": "Brief description for your profile.",
            "class": "input",
            "id": "bio",
            "type":"textarea",
            "style":"width: 100%;  padding: 0 18px; border:none; resize: none",
            "cols": "55",
            "rows": "10"
         }
      )
   )

   city = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "",
         "class": "input",
         "id": "city",
         "type": "text",
      }
      )
   )

   address = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
      attrs={
         "placeholder": "3 Saka Street, Lagos, Nigeria",
         "class": "input",
         "id": "address",
         "type": "text",
      }
      )
   )

   date_of_birth = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "input profileDate bg-white",
            "placeholder":"Date of Birth",
            "id": 'date_of_birth'
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
            'class': 'input',
            'id': 'gender'
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
         "job_title",
         "bio",
         "city",
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
            "job_title",
            "bio",
            "city",
            "address",
            "mobile_no",
            "date_of_birth",
            "gender",  
         ):
            self.fields[fieldname].help_text = None

class UserSocialHandleForm(forms.ModelForm):

   facebook = forms.URLField(
      label='',
      required=False,
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.facebook.com/',
            "class": 'input',
            "id": 'facebook_handle'
         }
      )
   )

   linkedin = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.linkedin.com/',
            "class": 'input',
            "id": 'linkedin_handle'
         }
      )
   )

   twitter = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.twitter.com/ ',
            "class": 'input',
            "id": 'twitter_handle'
         }
      )
   )

   instagram = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.instagram.com/',
            "class": 'input',
            "id": 'instagram_handle'
         }
      )
   )

   youtube = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.youtube.com/',
            "class": 'input',
            "id": 'youtube_handle'
         }
      )
   )

   behance = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://www.behance.net/',
            "class": 'input',
            "id": 'behance_handle'
         }
      )
   )

   dribbble = forms.URLField(
      label='',
      required=False,      
      widget=forms.URLInput(
         attrs={
            "placeholder": 'https://dribbble.com/',
            "class": 'input',
            "id": 'dribbble_handle'
         }
      )
   )


   class Meta:
      model = SocialHandle
      fields = (
         'facebook',
         'linkedin',
         'twitter',
         'instagram',
         'youtube',
         'behance',
         'dribbble'
      )
      