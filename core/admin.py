from django.contrib import admin
from .models import Video, Comment, Channel, Like, Dislike, Video_View, Channel_Subscription, Category, PageContents, About, Contact, ContactInfo
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user','category']
    list_filter = ('user', 'category')
    class Meta:
        model = Video
        
admin.site.register(Video, VideoAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'video']
    class Meta:
        model = Like

admin.site.register(Like, LikeAdmin)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'video']
    class Meta:
        model = Dislike

admin.site.register(Dislike, DislikeAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'video']
    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_name', 'channel_price', 'subscribers', 'user']
    class Meta:
        model = Channel

admin.site.register(Channel, ChannelAdmin)


admin.site.register([Video_View, Channel_Subscription, PageContents, About, Contact, ContactInfo])
