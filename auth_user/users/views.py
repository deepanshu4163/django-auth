from django.shortcuts import redirect, render
from django.contrib import messages
from users.forms import UserRegisterForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User Created for {username}')
            return redirect('home')
    else:        
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})