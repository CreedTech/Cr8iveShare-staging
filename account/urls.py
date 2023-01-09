from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register/creator', views.creator_register, name="creator_register"),
    path('logout/', views.user_logout, name="logout"),
]
