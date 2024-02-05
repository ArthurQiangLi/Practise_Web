""" define learning_logs's url mode"""
from django.urls import re_path, path
from . import views # '.' means current dicrectory

app_name = 'learning_logs'  # Define the app name here

urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r"^topics/$", views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]