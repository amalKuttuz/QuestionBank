from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', user_views.home, name='index'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
    
     ]