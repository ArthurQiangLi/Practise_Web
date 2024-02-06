"""defing url mode for this application"""

from django.urls import re_path, path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout')
]