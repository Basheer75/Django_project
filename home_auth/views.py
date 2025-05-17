from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.utils.crypto import get_random_string
from .models import PasswordResetRequest  # Ensure this import is correct
from django.conf import settings

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        role = request.POST.get('role', '')

        username = email  # Ensure unique username

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'authentication/register.html')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True

        user.save()
        login(request, user)
        messages.success(request, "Signup successfully!")
        return redirect('index')

    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')

            if user.is_admin:
                return redirect("admin_dashboard")
            elif user.is_teacher:
                return redirect("teacher_dashboard")
            elif user.is_student:
                return redirect("dashboard")
            else:
                messages.error(request, 'Invalid user role')
                return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'authentication/login.html')


def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, 'Reset link sent to your email.')
        else:
            messages.error(request, 'Email not found')

    return render(request, 'authentication/forgot-password.html')


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()

    if not reset_request or not reset_request.is_valid():
        messages.error(request, "Invalid or expired reset link")
        return redirect('index')

    if request.method == "POST":
        new_password = request.POST.get('new_password')
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'Password reset successful')
        return redirect('login')

    return render(request, 'authentication/reset_password.html', {'token': token})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
