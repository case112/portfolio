from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_otp.admin import OTPAdminSite

from posts.views import index, blog, post, about, InstaView

admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index),
    path('insta/', InstaView.as_view()),
    path('about/', about),
    path('blog/', blog, name='post-list'),
    path('post/<slug>/', post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
