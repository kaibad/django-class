from django.contrib import admin
from .models import Profile, User,Like, Note, Post, Student,NoteStudentFav

# Register your models here.
admin.site.register(Note)
admin.site.register(Student)
admin.site.register(NoteStudentFav)

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
