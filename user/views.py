from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from upload.forms import BookAddForm
from upload.models import Book
from.filter import FilterClass

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def download(request):
    ordered=Book.objects.filter(approval=True).order_by('course')
    myfilter=FilterClass(request.GET,queryset=ordered)
    ordered=myfilter.qs

    context={'ordered':ordered,'myfilter':myfilter}
    return render(request, 'download.html',context)

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
            messages.success(request, "Submitted for approval")
            return redirect('index')
        else:
            messages.error(request, "error occured while adding")
            return redirect('index')
    else:
        form = BookAddForm()
        return render(request, 'questionsite.html', {'form': form})