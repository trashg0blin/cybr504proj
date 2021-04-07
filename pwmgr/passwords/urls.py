from django.urls import re_path,path
from pwmgr import settings
from django.conf.urls.static import static
from . import views

app_name='passwords'

urlpatterns=[
    path('', views.password_home, name='home'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_password/', views.create_password, name='create_password'),
]