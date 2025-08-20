from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('admin-panel/dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.admin_logout, name='logout'),
    path('admin-panel/profile/', views.admin_profile, name='admin_profile'),


]
