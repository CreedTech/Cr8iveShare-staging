from django import forms
from django.utils.safestring import mark_safe

from .models import Category


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
                "cols": "55%",
                "rows": "10"
            }
        )
    )
    file = forms.FileField()
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
    channel_image = forms.ImageField(max_length=50)
    channel_price = forms.CharField(
        widget=forms.NumberInput()
    )
    # username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # suscribers = models.IntegerField(default=0, blank=False, null=False)
