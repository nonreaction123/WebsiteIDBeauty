from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Home page
def home(request):
    return render(request, 'main/homepage.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect(reverse('superuser_view'))
            elif user.is_staff:
                return HttpResponseRedirect(reverse('admin_view'))
            else:
                return HttpResponseRedirect(reverse('normal_user_view'))
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'main/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# Superuser view
@login_required
def superuser_view(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request, 'main/superuser_view.html')

# Admin view
@login_required
def admin_view(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'main/admin_view.html')

# Normal user view
@login_required
def normal_user_view(request):
    return render(request, 'main/normal_user_view.html')