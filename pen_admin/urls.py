from django.urls import path
from . import views

app_name = 'pen_admin'

urlpatterns = [
   path('', views.dashboard, name="dashboard"),
   path('/creators', views.creators, name="creators"),
   
   
   # Videos
   path('video/', views.video, name='video'),
   path('video/add/', views.add_video, name='add_video'),      
   path('video/edit/<slug:slug>/', views.edit_video, name='edit_video'),
   path('video/delete/<slug:slug>/', views.delete_video, name='delete_video'),
]