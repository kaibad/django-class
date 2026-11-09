from django.contrib import admin
from .models import Note, Student,NoteStudentFav

# Register your models here.
admin.site.register(Note)
admin.site.register(Student)
admin.site.register(NoteStudentFav)