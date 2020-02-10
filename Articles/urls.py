from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list_view, name='articles'),
    url(r'^create_article/$', views.create_article, name='createArticle'),
    url(r'^edit_article/$', views.edit_article, name='editArticle'),
    url(r'save_changes/$', views.save_changes, name="saveChanges"),
    url(r'^delete_article/$', views.delete_article, name="deleteArticle"),
    url(r'^(?P<slug>[\w-]+)$', views.article_detail, name='articleDetail'),
]
