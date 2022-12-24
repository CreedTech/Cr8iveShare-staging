from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from pages.models import ContactDetail, Subscriber
from account.models import User

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
