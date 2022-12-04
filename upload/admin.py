from django.contrib import admin

# Register your models here.
from .models import Book


class ModelBook(admin.ModelAdmin):
    list_display = ('papername', 'course','university', 'sem','approval','addedon','addedby', 'pdf')
    search_fields = ('course', 'papername')
    list_filter = ('course', 'addedby')


admin.site.register(Book, ModelBook)