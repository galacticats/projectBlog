from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^articles/', include('Articles.urls')),
    url(r'^$', views.homepage_view),
    url(r'^about/$', views.about_view, name='about'),
    url(r'^accounts/', include('Accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
