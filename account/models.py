from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify


class User(AbstractUser):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('not_saying', 'Prefer not to say'),
    )
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_images',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'png', 'jpg', 'jpeg', 'webp'
                ]
            )
        ]
    )
    background_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_bg_images',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                  'png', 'jpg', 'jpeg', 'webp'
                ]
            )
        ]
    )
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    mobile_no = models.CharField(max_length=14, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=gender_choices, null=True)
    slug = AutoSlugField(
        unique=True, populate_from='username', sep='_', null=True)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
        


# @receiver(pre_delete, sender=User)
# def user_image_delete(sender, instance, **kwargs):
#     instance.file.delete(False)


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    request_creator_access = models.BooleanField(
        null=True, blank=True, default=False)
    is_verified = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f'User settings for {self.user.username}'

    class Meta:
        verbose_name = "User Setting"
        verbose_name_plural = "User Settings"

