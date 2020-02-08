from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list_view, name='articles'),
    url(r'^(?P<slug>[\w-]+)$', views.article_detail, name='articleDetail')
]
