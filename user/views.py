from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from upload.forms import BookAddForm

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST,request.FILES)
        print(form)

        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, "Added successfully")
            return redirect('index')
        else:
            messages.error(request, "error occured while adding")
            return redirect('index')
    else:
        form = BookAddForm()
        return render(request, 'questionsite.html', {'form': form})