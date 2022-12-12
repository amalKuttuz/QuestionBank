from django import forms
from .models import Book,Booklist


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['papername','sem','university', 'course', 'pdf']

class Updatebook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class searchbook(forms.ModelForm):
    class Meta:
        model = Booklist
        fields = '__all__'