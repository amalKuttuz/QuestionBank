from django import forms
from .models import Book


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['papername','sem','university', 'course', 'pdf']

class Updatebook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'