from django.urls import re_path, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<input_value>\w+)?', views.results, name='results'),
]
