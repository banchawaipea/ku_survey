from django.contrib import admin
from django.urls import path, include

# add Static file config
# from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    # ******* Deploy settings *******

    # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # ******* End Deploy settings *******

    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
