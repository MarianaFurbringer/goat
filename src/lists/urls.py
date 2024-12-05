from django.urls import path
from lists import views

urlpatterns = [
    path(r'^new$', views.new_list, name='new_list'),
    path(r'^(\d+)/$', views.view_list, name='view_list'),
]