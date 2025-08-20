from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User



# Check if user is admin
def is_admin(user):
    return user.is_superuser

# Admin login view
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials or not an admin.")
    return render(request, 'admin_panel/login.html')

# Dashboard view (admin only)
@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def admin_profile(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update user details
        user.username = username
        user.email = email
        user.save()
        messages.success(request, 'Profile updated successfully!')

    return render(request, 'admin_panel/profile.html', {'user': user})