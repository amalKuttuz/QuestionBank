from django.db import models
from moderator.models import *
# Create your models here.
class Book(models.Model):
    papername = models.CharField(max_length=100,null=True)
    addedby = models.CharField(max_length=100,null=True)

    sem=models.ForeignKey(Semesters, on_delete=models.CASCADE,null=True)
    pdf = models.FileField(upload_to='pdf/',null=True)
    approval=models.BooleanField(default= False,null=True)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE,null=True)
    addedon=models.TimeField(auto_now_add=True,null=True)
    # addedby=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    university=models.ForeignKey(Universities, on_delete=models.CASCADE,null=True)

    # def delete(self, *args, **kwargs):
    #     self.cover.delete()
    #     self.pdf.delete()
    #     super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.papername

class Booklist(models.Model):
    pname=models.ForeignKey(Book, on_delete=models.CASCADE)
    semname=models.ForeignKey(Semesters, on_delete=models.CASCADE,null=True)
    coursename=models.ForeignKey(Courses, on_delete=models.CASCADE,null=True)
    universityname=models.ForeignKey(Universities, on_delete=models.CASCADE,null=True)
 