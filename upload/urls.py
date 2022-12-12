from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('/', views.home, name='home'),
    path('/add', views.add_book, name='add_book'),
    path('/update/<int:pk>',views.modify_book,name="update"),
    path('/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('view-pdf/<int:pk>/', views.pdf_view,name='pdf_view'),
    path('/result', views.question, name='result'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')


]