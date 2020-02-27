from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^account/$', views.account_view, name="account"),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^changePassword$', views.change_password_view, name="changePassword"),
    url(r'^deleteAccount$', views.delete_account_view, name="deleteAccount"),
]