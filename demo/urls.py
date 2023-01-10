from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from accounts.views import *
from django.views.generic import TemplateView, RedirectView
from users.views import author_external
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('froala_editor/', include('froala_editor.urls')),
    path('pen_admin/', admin.site.urls),
    # path('accounts/', RedirectView.as_view(url='/account')),
     path('auth/', include('account.urls')),
     path('@<slug:slug>/', include('users.urls')),
    path('', include('core.urls')),
    #  path('', include('pages.urls')),
    path('author/<slug:slug>/', author_external, name='author_external'),
    # path('admin/', admin.site.urls),
    # path('account/', include("accounts.urls")),
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
handler404 = 'core.views.Page_404'