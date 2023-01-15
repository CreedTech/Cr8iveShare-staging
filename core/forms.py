from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.mail import send_mail
from .models import Category, Contact


class CommentForm(forms.Form):
    comment = forms.CharField(label='comment', max_length=500,
                           widget=forms.Textarea(
                               attrs={
                                   "style":"width: 100%; height: 72px; padding: 5px 18px;"
                               }
                           ))
    # video = forms.IntegerField(widget=forms.HiddenInput(), initial=1)


class NewVideoForm(forms.Form):
    title = forms.CharField(label=' Video Title', max_length=50)
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "style": "border: none",
                "cols": "55",
                "rows": "10"
            }
        )
    )
    file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "type": "file",
              "placeholder": "",
                "accept":"video/mp4,video/x-m4v,video/*",
                "id": "file",
                "onchange": "loadFile(event)"
            }
        )
    )
    banner = forms.ImageField(
        label="",
        widget=forms.FileInput(
            attrs={
              "type": "file",
              "placeholder": "",
                "accept": "image/*",
                "id": "banner",
                "onchange": "loadFile(event)"
            }
        ),
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(
        attrs={
            "type": "select",
            "placeholder": "",
            "style":"width: 100%; height: 42px; padding: 0 18px; border:none;"
        }
    ),)


class ChannelForm(forms.Form):
    channel_name = forms.CharField(max_length=50, label='Channel Name')
    channel_image = forms.ImageField(max_length=50,widget=forms.FileInput(
            attrs={
              "type": "file",
              "placeholder": "",
                "accept": "image/*",
                "id": "banner",
                "onchange": "loadFile(event)"
            }
        ),)
    channel_price = forms.CharField(
        widget=forms.NumberInput()
    )
    # username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # suscribers = models.IntegerField(default=0, blank=False, null=False)


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=120,
        widget=forms.TextInput(
                attrs={
                    "placeholder": "Your name *",
                    "class": "wpcf7-form-control wpcf7-text wpcf7-validates-as-required",
                    "type": "text"
                }
            )
        )
    email = forms.EmailField(
        widget=forms.TextInput(
                attrs={
                    "placeholder": "Your Email *",
                    "class": "wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email",
                    "type":"email"
                }
            )
        )
    subject = forms.CharField(
        widget=forms.TextInput(
                attrs={
                    "placeholder": "Subject",
                    "class": "wpcf7-form-control wpcf7-text",
                    "type": "text"
                }
            )
    )
    message = forms.CharField(
        widget=forms.Textarea(
                attrs={
                    "placeholder": "Your Message...",
                    "class": "wpcf7-form-control wpcf7-textarea",
                    "type": "textarea",
                    "row": 5,
                    "col": 40
                }
            )
    )

    class Meta:
        model = Contact
        fields = '__all__'

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.cleaned_data["email"]]
        )