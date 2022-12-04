from django.contrib import admin
from .models import *
# Register your models here.
class UniversityAdmin (admin.ModelAdmin):
    list_display=('universityname','id')
admin.site.register(Universities,UniversityAdmin)

class Coursesadmin (admin.ModelAdmin):
    list_display=('coursename','university')
admin.site.register(Courses,Coursesadmin)

# class Typeadmin (admin.ModelAdmin):
#     list_display=('typename','course')
# admin.site.register(Type,Typeadmin)

class semadmin (admin.ModelAdmin):
    list_display=('semestername','id')
admin.site.register(Semesters,semadmin)

# class Papersadmin (admin.ModelAdmin):
#     list_display=('papername','semester')
# admin.site.register(Papers,Papersadmin)

# class PrevQstnsadmin (admin.ModelAdmin):
#     list_display=('description','fileloc','addedby','addedon','approval','course','sem')
# admin.site.register(PrevQstns,PrevQstnsadmin)