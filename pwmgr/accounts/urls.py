from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountsHome.as_view(), name='home'),
    path('register/', views.create_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
