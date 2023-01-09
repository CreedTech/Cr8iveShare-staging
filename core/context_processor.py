from .models import *
from django.db.models import Q
# from moviepy.editor import VideoClipFile
import random
from django.shortcuts import redirect, render, get_object_or_404


def post_renderer(request):
    page_contents = PageContents.objects.latest(
        'updated') if PageContents.objects.all().count() > 0 else None
    category = Category.objects.all()
    channel_count = Channel.objects.all().count()
    videos = Video.objects.filter(
        user__username=request.user).order_by("-datetime")
    all_videos = Video.objects.all()
    comments = Comment.objects.filter(
        user__username=request.user).order_by("-datetime")
    number_of_views = Video_View.objects.filter(
        user__username=request.user)
    # most_recent_channels = Channel.objects.exclude(user=user)
    user_videos_length = len(videos)
    all_videos_length = len(all_videos)
    user_comment_length = len(comments)
    user_video_views_length = len(number_of_views)
    you_may_also_like_videos = Video.objects.all().order_by("-datetime")[:8]
    latest_videos = Video.objects.order_by('-datetime')[:5]
    # user_object = User.objects.get(username=user.username)
    # video_file = request.FILES.get('video')
    counts = []
    for c in category:
        category_count = Video.objects.filter(category=c).count()
        counts.append(category_count)

    category_count = zip(category, counts)
    most_recent_videos = Video.objects.order_by('-datetime')[:8]
    home_side_videos = Video.objects.order_by('?')[:3]
    home_carousel_videos = Video.objects.order_by('?')[:8]
    top_videos = Video.objects.order_by('-number_of_views')[:4]
    
    # most_recent_videos = Video.objects.order_by('-datetime')[:8]
    most_recent_channels = Channel.objects.exclude(user=request.user)[:2] if request.user.is_authenticated else None
    footer_channels = Channel.objects.exclude(user=request.user)[:3] if request.user.is_authenticated else None
    # price_for_channel = Channel.objects.filter(price=34)

    channel = False
    if request.user.username != "":
        # print("YEs")
        try:
            channel = Channel.objects.filter(user=request.user)
            print(channel)
            print("Yo")
            channel = channel.get()
        except Channel.DoesNotExist:
            channel = False

    # post = get_object_or_404(Post, slug=slug)
    # category = Category.objects.all()
    # counts = []
    # for c in category:
    #     category_count = Post.objects.filter(category=c).count()
    #     counts.append(category_count)

    # category_count = zip(category,counts)
    # side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    # side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]

    return {
        'you_may_also_like_videos': you_may_also_like_videos,
        'all_videos': all_videos,
        'page_contents': page_contents,
        'cat_count': category_count,
        'channel_count': channel_count,
        'most_recent_videos': most_recent_videos,
        'home_side_videos': home_side_videos,
        'home_carousel_videos': home_carousel_videos,
        'top_videos': top_videos,
        'user_videos_length': user_videos_length,
        'all_videos_length': all_videos_length,
        'user_comment_length': user_comment_length,
        'user_video_views_length': user_video_views_length,
        # 'user_object': user_object,
        'most_recent_channels': most_recent_channels,
        'footer_channels': footer_channels,
        'channel': channel,
        "latest_videos": latest_videos,
        # 'posts': post,
    }

