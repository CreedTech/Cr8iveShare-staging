from django.urls import path
from . import views
from pen_admin import views as admin_views


app_name = 'users'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('profile/', views.user_profile, name="profile"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('delete-account', views.delete_account, name='delete_account'),


    # Admin Views
    path('staffs/', admin_views.staffs, name="staffs"),
    path('staff__<str:username>/', admin_views.staff_single, name='single_staff'),
    path('creators/', admin_views.creators, name="creators"),
    path('creator__<str:username>/', admin_views.creator_single, name='single_creator'),
    path('viewers/', admin_views.viewers, name="viewers"),
    path('viewer__<str:username>/', admin_views.viewer_single, name='single_viewer'),
    # path('subscribers/', admin_views.subscribers, name="subscribers"),
    # path('subscriber/delete/<int:id>/', admin_views.delete_subscriber, name="delete_subscriber"),
]
