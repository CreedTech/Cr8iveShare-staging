from django.shortcuts import render, redirect, HttpResponseRedirect,get_object_or_404
from django.contrib import messages
from core.forms import ChannelForm, CommentForm, NewVideoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# from pages.models import ContactDetail, Subscriber
from account.models import User
from django.core.paginator import Paginator
from core.models import Category, Comment, Dislike, FollowersCount, Like, Video, Channel, Channel_Subscription, Video_View, PageContents
from core.forms import NewVideoForm


@login_required
def dashboard(request):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return redirect('home')
    else:
        total_users = len(User.objects.all().filter(is_staff=False))
        total_videos = len(Video.objects.all())
        total_categories = len(Category.objects.all())
        total_channel_subscription = len(Channel_Subscription.objects.all())
        total_channels = len(Channel.objects.all())
        total_comment = len(Comment.objects.all())
        total_dislikes = len(Dislike.objects.all())
        total_likes = len(Like.objects.all())
        total_page_contents = len(PageContents.objects.all())
        total_video_views = len(Video_View.objects.all())

        context = {
            'total_users': total_users,
            'total_videos': total_videos,
            'total_categories': total_categories,
            'total_channel_subscription': total_channel_subscription,
            'total_channels': total_channels,
            'total_comment': total_comment,
            'total_dislikes': total_dislikes,
            'total_likes': total_likes,
            'total_page_contents': total_page_contents,
            'total_video_views': total_video_views,
        }
        return render(request, 'pen_admin/dashboard.html', context)

# =========================================================== videos ===========================================================
# View for all videos


@login_required
def video(request):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return redirect('home')
    else:
        videos = Video.objects.all()
        p = Paginator(videos, 2)
        page = request.GET.get('page')
        paginated_videos = p.get_page(page)

        context = {
            'paginated_videos': paginated_videos,
        }
        return render(request, 'pen_admin/videos/videos.html', context)


@login_required
def add_video(request):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return redirect('index')
    else:
        if request.method == 'POST':
            add_video_form = NewVideoForm(request.POST, request.FILES)
            if add_video_form.is_valid():
                title = add_video_form.cleaned_data['title']
                description = add_video_form.cleaned_data['description']
                path = add_video_form.cleaned_data['file']
                banner = add_video_form.cleaned_data['banner']
                category = add_video_form.cleaned_data['category']
                add_video_form = Video(title=title,
                              description=description,
                              user=request.user,
                              path=path,
                              number_of_views=0,
                              banner=banner,
                              category=category,
                              datetime=timezone.now())
                add_video_form.save()
                messages.success(request, 'video added successfully')
                return redirect('pen_admin:video')
            else:
                messages.error(request, "An error occured")
                return redirect('pen_admin:video')
        else:
            add_video_form = NewVideoForm()
        context = {
            'add_video_form': add_video_form
        }
        return render(request, 'pen_admin/videos/add_video.html', context)


@login_required
def edit_video(request, slug):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return redirect('home')
    else:
        video = get_object_or_404(Video, slug=slug)
        if request.method == 'POST':
            add_video_form = NewVideoForm(
                request.POST or None, request.FILES, instance=video)
            if add_video_form.is_valid():
                add_video_form.save()
                messages.success(request, 'video Updated successfully')
                return redirect('pen_admin:videos')
            else:
                messages.error(request, "An error occured")
                return redirect('pen_admin:videos')
        else:
            add_video_form = NewVideoForm(instance=video)
        context = {
            'add_video_form': add_video_form,
            'video': video
        }
        return render(request, 'pen_admin/videos/edit_video.html', context)


@login_required
def delete_video(request, slug):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return redirect('home')
    else:
        video = get_object_or_404(video, slug=slug)
        video.delete()
        messages.success(request, 'video deleted successfully')
        return redirect('videos')

# ! Staffs


@login_required
def staffs(request, slug):
    if not request.user.is_superuser:
        messages.warning(request, 'You are not authorized to access that page')
        return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
    else:
        staffs = User.objects.filter(is_staff=True)
        context = {
            'staffs': staffs
        }
        return render(request, 'pen_admin/staffs.html', context)


@login_required
def staff_single(request, slug, username):
    if not request.user.is_superuser:
        messages.warning(request, 'You are not authorized to access that page')
        return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
    else:
        staff = User.objects.filter(is_staff=True).get(username=username)
        context = {
            'staff': staff
        }
        return render(request, 'pen_admin/single_staff.html', context)

# ! creators


@login_required
def creators(request, slug):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
    else:
        creators = User.objects.filter(is_creator=True)
        context = {
            'creators': creators
        }
        return render(request, 'pen_admin/creators.html', context)


@login_required
def creator_single(request, slug, username):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
    else:
        creator = User.objects.filter(is_creator=True).get(username=username)
        context = {
            'creator': creator
        }
        return render(request, 'pen_admin/single_creator.html', context)


# ! viewers
@login_required
def viewers(request, slug):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
    else:
        viewers = User.objects.filter(is_creator=False)

        context = {
            'viewers': viewers
        }
        return render(request, 'pen_admin/viewers.html', context)


@login_required
def viewer_single(request, slug, username):
    if not request.user.is_staff:
        messages.warning(request, 'You are not authorized to access that page')
        return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
    else:
        viewer = User.objects.filter(is_creator=False).get(username=username)
        context = {
            'viewer': viewer
        }
        return render(request, 'pen_admin/single_viewer.html', context)


# ! Subscribers
# @login_required
# def subscribers(request, slug):
#    if not request.user.is_staff:
#       messages.warning(request, 'You are not authorized to access that page')
#       return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
#    else:
#       subscribers = Subscriber.objects.all()
#       context = {
#          'subscribers': subscribers
#       }
#       return render(request, 'pen_admin/subscribers.html', context)


# @login_required
# def delete_subscriber(request, slug, id):
#    if not request.user.is_staff:
#       messages.warning(request, 'You are not authorized to access that page')
#       return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
#    else:
#       subscriber = Subscriber.objects.get(id=id)
#       subscriber.delete()
#       messages.success(request, 'Subscriber deleted!')
#       return redirect('users:subscribers')
