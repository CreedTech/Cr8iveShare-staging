from .models import *
from django.db.models import Q
# from moviepy.editor import VideoClipFile

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
        user__username=request.user).order_by("-datetime")
    # most_recent_channels = Channel.objects.exclude(user=user)
    user_videos_length = len(videos)
    all_videos_length = len(all_videos)
    user_comment_length = len(comments)
    user_video_views_length = len(number_of_views)
    # user_object = User.objects.get(username=user.username)
    # video_file = request.FILES.get('video')
    counts = []
    for c in category:
        category_count = Video.objects.filter(category=c).count()
        counts.append(category_count)

    category_count = zip(category, counts)
    most_recent_videos = Video.objects.order_by('-datetime')[:8]
    
    # most_recent_videos = Video.objects.order_by('-datetime')[:8]
    most_recent_channels = Channel.objects.exclude(user=request.user) if request.user.is_authenticated else None

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
        'page_contents': page_contents,
        'cat_count': category_count,
        'channel_count': channel_count,
        'most_recent_videos': most_recent_videos,
        'user_videos_length': user_videos_length,
        'all_videos_length': all_videos_length,
        'user_comment_length': user_comment_length,
        'user_video_views_length': user_video_views_length,
        # 'user_object': user_object,
        'most_recent_channels': most_recent_channels,
        'channel': channel
        # 'posts': post,
    }

