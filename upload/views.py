from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Book
from .forms import BookAddForm,Updatebook
from django.contrib import messages

@staff_member_required
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

@staff_member_required
def add_book(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST,request.FILES)
        print(form)

        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, "Book added successfully")
            return redirect('home')
        else:
            messages.error(request, "error")
            return redirect('home')
    else:
        form = BookAddForm()
        return render(request, 'add_book.html', {'form': form})

@staff_member_required
def delete_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        messages.success(request, "Book deleted successfully")
        return redirect('home')
    else:
        return redirect('home')
        
@staff_member_required
def modify_book(request, pk):
        q=Book.objects.get(id=pk)
        form=Updatebook(instance=q)
        context={
                    'form':form

                } 
        if request.method=='POST':
            form=Updatebook(request.POST,request.FILES,instance=q)
            if form.is_valid():
                form.save()
                context={
                    'form':form

                        }  
                messages.success(request,"Details Updated")
                return redirect('home')
            else:
                messages.error(request,"An error occured")
                return redirect('home')
        return render(request,'update.html',context)  

def pdf_view(request,pk):
    # q=Book.objects.get(id=pk)
    q=Book.objects.values_list('pdf', flat=True).get(id=pk)
    import os
    filepath = os.path.join('media', q)

    with open(filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response   
