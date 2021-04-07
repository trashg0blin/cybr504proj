from django.urls import re_path,path
from pwmgr import settings
from django.conf.urls.static import static
from . import views

app_name='passwords'

urlpatterns=[
    path('', views.password_home, name='home'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_password/', views.create_password, name='create_password'),
    path('detail/<int:pk>', views.detail_password, name='detail_password'),
    path('update_hints/<int:pk>', views.update_hints, name='update_hints'),
    path('update_password/<int:pk>', views.update_password, name='update_password'),
    path('delete_password/<int:pk>', views.delete_password, name='delete_password'),
    path('create_generated_password/', views.create_generated_password, name='create_generated_password'),
    path('update_generated_password/<int:pk>', views.update_generated_password, name='update_generated_password'),
    path('delete_generated_password/<int:pk>', views.delete_generated_password, name='delete_generated_password'),
    path('generated_passwords/', views.list_generated_password, name='generated_passwords'),

]