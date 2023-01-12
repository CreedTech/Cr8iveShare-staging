from django.db import models
# from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
import uuid
from django.utils import timezone
from account.models import User


# from Users.models import User


class PageContents(models.Model):
    page_name = models.CharField(max_length=20, default="SplitUnity")
    navbar_logo = models.ImageField(
        upload_to='page_contents/', null=True, blank=True, default="https://dummyimage.com/99x24")
    footer_logo = models.ImageField(
        upload_to='page_contents/', null=True, blank=True, default="https://dummyimage.com/99x24")
    footer_description = models.CharField(
        max_length=500, null=True, blank=True, default="Lorem ipsum dolor sit amet consectetur adipiscing elit platea convallis tortor, et laoreet posuere nisi suspendisse mollis gravida facilisi fusce cras, augue dictumst tempor imperdiet lacus risus neque elementum nisl.")
    footer_address = models.CharField(
        max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet consectetur, adipiscing elit platea nec.")
    footer_phone = models.CharField(
        max_length=20, null=True, blank=True, default="+123456789")
    footer_email = models.CharField(
        max_length=50, null=True, blank=True, default="lorem@lorem.com")
    social_icon_1 = models.CharField(
        max_length=30, null=True, blank=True, default="twitter")
    social_icon_url_1 = models.URLField(
        max_length=200, default='https://google.com')
    social_icon_2 = models.CharField(
        max_length=30, null=True, blank=True, default="facebook")
    social_icon_url_2 = models.URLField(
        max_length=200, default='https://google.com')
    social_icon_3 = models.CharField(
        max_length=30, null=True, blank=True, default="youtube")
    social_icon_url_3 = models.URLField(
        max_length=200, default='https://google.com')
    social_icon_4 = models.CharField(
        max_length=30, null=True, blank=True, default="instagram")
    social_icon_url_4 = models.URLField(
        max_length=200, default='https://google.com')
    updated = models.DateTimeField(auto_now=True)
    footer_social_icon_1 = models.CharField(
        max_length=30, null=True, blank=True, default="facebook-f")
    footer_social_icon_url_1 = models.URLField(
        max_length=200, default='https://google.com')
    footer_social_icon_2 = models.CharField(
        max_length=30, null=True, blank=True, default="twitter")
    footer_social_icon_url_2 = models.URLField(
        max_length=200, default='https://google.com')
    footer_social_icon_3 = models.CharField(
        max_length=30, null=True, blank=True, default="instagram")
    footer_social_icon_url_3 = models.URLField(
        max_length=200, default='https://google.com')
    footer_social_icon_4 = models.CharField(
        max_length=30, null=True, blank=True, default="youtube")
    footer_social_icon_url_4 = models.URLField(
        max_length=200, default='https://google.com')
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name = ("PageContent")
        verbose_name_plural = ("PageContents")


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = self.name
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    banner = models.ImageField(
        upload_to='video_banner', default='/static/1600x900.png')
    path = models.FileField(upload_to='videos/')
    datetime = models.DateTimeField(auto_now_add=True,
                                    blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_views = models.IntegerField(blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Video")
        verbose_name_plural = ("Videos")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Video_detail", kwargs={"pk": self.pk})


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user


class FollowersCount(models.Model):
    followers = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"{self.user}  ---  {self.comment}"

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})


class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    channel_image = models.ImageField(
        upload_to='channel_images/', null=True, blank=True, default="https://dummyimage.com/1600x900")
    channel_price = models.DecimalField(max_digits=10, decimal_places=2)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class Video_View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)


class Channel_Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True,
                               default="Lorem ipsum dolor sit amet, consectetur adip")
    description = models.CharField(max_length=700, null=True, blank=True,
                                   default="Lorem ipsum dolor sit amet, consectetur adip dolor sit amet dolore magna aliquet dolore magna aliquet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum d lorem ipsum dolor sit amet lorem ipsum d")
    user_image_1 = models.ImageField(
        upload_to='about_images', null=True, blank=True, default='/static/1600x900.png')
    user_image_2 = models.ImageField(
        upload_to='about_images', null=True, blank=True, default='/static/1600x900.png')
    user_image_3 = models.ImageField(
        upload_to='about_images', null=True, blank=True, default='/static/1600x900.png')
    user_name_1 = models.CharField(max_length=20, null=True, blank=True)
    user_name_2 = models.CharField(max_length=20, null=True, blank=True)
    user_name_3 = models.CharField(max_length=20, null=True, blank=True)
    user_occupation_1 = models.CharField(max_length=50, null=True, blank=True)
    user_occupation_2 = models.CharField(max_length=50, null=True, blank=True)
    user_occupation_3 = models.CharField(max_length=50, null=True, blank=True)
    user_social_media_link_1_facebook = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_1_twitter = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_1_instagram = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_2_facebook = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_2_twitter = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_2_instagram = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_3_facebook = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_3_twitter = models.URLField(
        max_length=200, default='https://google.com')
    user_social_media_link_3_instagram = models.URLField(
        max_length=200, default='https://google.com')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class ContactInfo(models.Model):
    '''Model definition for ContactInfo.'''
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    second_email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=30)
    second_phone_number = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta definition for ContactInfo.'''

        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfos'

    def __str__(self):
        return f'{self.email} ------------- {self.phone_number}'


class Contact(models.Model):
    '''Model definition for Contact.'''
    name = models.CharField(max_length=100, help_text='John Doe')
    email = models.EmailField(max_length=254, help_text="example@example.com")
    subject = models.CharField(max_length=100, help_text="Contact subject...")
    message = models.TextField(help_text='My name is...')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta definition for Contact.'''

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.name} ------------- {self.email} on {self.created_at}'
