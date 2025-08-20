"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include('admin_panel.urls')),
    
    # Password Change (logged-in admin)
    path('admin-panel/password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='admin_panel/password_change.html'), 
         name='password_change'),
    path('admin-panel/password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='admin_panel/password_change_done.html'), 
         name='password_change_done'),

    # Password Reset (forgot password)
    path('admin-panel/password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='admin_panel/password_reset.html'), 
         name='password_reset'),
    path('admin-panel/password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='admin_panel/password_reset_done.html'), 
         name='password_reset_done'),
    path('admin-panel/reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='admin_panel/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('admin-panel/reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='admin_panel/password_reset_complete.html'), 
         name='password_reset_complete'),
]


