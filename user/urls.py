from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from upload.views import home
from user import views as user_views

urlpatterns = [
    path('upload', home, name='adminpanel'),
    path('admin/', admin.site.urls),
    path('', user_views.home, name='index'),
    path('blog', user_views.blog, name='blog'),
    path('download', user_views.download, name='download'),
    path('contact', user_views.contact, name='contact'),
    path('about', user_views.about, name='about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logoutnow'),
    path('add',user_views.add_book, name='addbook'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='accountslogin'),
    


     ]
     