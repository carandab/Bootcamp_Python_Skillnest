from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Usuario {username} creado con éxito!')
            login(request, user)  # Auto login después del registro
            return redirect('task_list')
        
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})