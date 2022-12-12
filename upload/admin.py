from django.contrib import admin

# Register your models here.
from .models import *


class ModelBook(admin.ModelAdmin):
    list_display = ('papername', 'course','university', 'sem','approval','addedon','addedby', 'pdf')
    search_fields = ('course', 'papername')
    list_filter = ('course', 'addedby')

class Booklists(admin.ModelAdmin):
    list_display = ('pname', 'coursename','universityname', 'semname')

admin.site.register(Book, ModelBook)
admin.site.register(Booklist, Booklists)