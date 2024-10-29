from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Get username from the form
        password = request.POST.get('password')  # Get password from the form
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, "There was an error logging in, please try again.")
            return redirect('home')  # Redirect back to the home page on error
    else:
        return render(request, 'home.html', {})  # Render the home page

def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('home')  # Redirect to the home page after logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Get username from the form
        password = request.POST.get('password')  # Get password from the form
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, "There was an error logging in, please try again.")
            return redirect('home')  # Redirect back to the home page on error
    else:
        return render(request, 'home.html', {})  # Render the home page

def register_user(request):
    return render(request, 'register.html', {}) 
