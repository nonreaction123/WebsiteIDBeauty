from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('superuser/', views.superuser_view, name='superuser_view'),
    path('admin/', views.admin_view, name='admin_view'),
    path('user/', views.normal_user_view, name='normal_user_view'),
]