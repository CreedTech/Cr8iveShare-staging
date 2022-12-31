from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from accounts.views import *
from django.views.generic import TemplateView, RedirectView
from users.views import author_external


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
]

handler404 = 'core.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
