from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomerProfile, SellerProfile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_customer:
                CustomerProfile.objects.create(user=user)
            elif user.is_seller:
                SellerProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.user.is_customer:
        profile = request.user.customer_profile
    elif request.user.is_seller:
        profile = request.user.seller_profile
    else:
        profile = None
    return render(request, 'accounts/profile.html', {'profile': profile})
