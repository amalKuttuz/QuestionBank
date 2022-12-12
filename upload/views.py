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

# def questionView(request,s):
#     # pd=Book.objects.values_list('papername','pdf', flat=False).get(course=s)
   
#     # return render(request,'result.html',{'pd':pd})


# def question(request):
#     selected_paper = None
#     selsem=None
#     selcourse=None
#     seluni=None
#     res = Book.objects.all()

    # if request.method == "POST":
    #     # Filter books by selected criteria, but only on a POST
    #     selected_paper = request.POST.get("p")
    #     # selsem = request.POST.get("sem")
    #     course = request.POST.get("course")
    #     # seluni = request.POST.get("university")
    #     # res = Book.filter(papername=selected_paper and selsem=sem and selcourse=course and seluni=university )
    #     # res = Book.objects.filter(papername=selected_paper,sem=selsem,course=selcourse,university=seluni)
    #     p=Book.objects.order_by('papername').values_list('papername', flat=True)
    #     selcourse=Book.objects.filter(coursenam=)

    # # Get a list of all unique pdf (group by paper)  
    #     # paper = Book.objects.order_by('papername').values_list('pdf', flat=True)
    #     paper=Book.objects.filter(papername=selected_paper)
    #     print(paper)
    # context = {

    #     'paper': paper,
    #     'res': res,
    #     'p':p, 
    #     'selected_paper': selected_paper,
    #     'selsem':selsem,
    #     'selcourse':selcourse,
    #     'seluni':seluni
        
    # }

    # return render(request, 'test.html', context)

def question(request):
    k=Book.objects.order_by('papername')
    return render(request, 'result.html', {'k':k})

