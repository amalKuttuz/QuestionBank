from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Universities(models.Model):
    universityname=models.CharField( max_length=100,null=True)

    def __str__(self):
        return self.universityname

class Courses(models.Model):
    coursename=models.TextField(null=True)
    university=models.ForeignKey(Universities, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.coursename

class Semesters(models.Model):
    semestername=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.semestername

# class Type(models.Model):
#     typename=models.CharField( max_length=50,null=True)
#     course=models.ForeignKey(Courses, on_delete=models.CASCADE,null=True)
#     semname=models.ForeignKey(Semesters, on_delete=models.CASCADE,null=True)
#     def __str__(self):
#         return self.typename


# class UG(models.Model):
#     semesters=models.CharField(max_length=50)
#     typeofsem=models.ForeignKey(Type, on_delete=models.CASCADE)

# class PG(models.Model):
#     semesters=models.CharField(max_length=50)
#     typeofsem=models.ForeignKey(Type, on_delete=models.CASCADE)



# class PrevQstns(models.Model):
#     description=models.TextField(null=True)
#     fileloc=models.FileField( upload_to='questions')
#     papername=models.TextField(null=True)
#     addedby=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     addedon=models.TimeField(auto_now_add=True)
#     approval=models.BooleanField(default= False)
#     course=models.ForeignKey(Courses, on_delete=models.CASCADE,null=True)
#     sem=models.ForeignKey(Semesters, on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.description

