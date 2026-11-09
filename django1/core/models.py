from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

class Note(models.Model):
    title = models.CharField(max_length=150)
    desciption = models.TextField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class NoteStudentFav(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

