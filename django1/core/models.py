
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

class User(models.Model):
    username = models.CharField(primary_key=True,unique=True,max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.username}"

class Profile(models.Model):

    class GENDER_CHOICES(models.TextChoices):
        MALE = 'M','Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'O', 'Others'

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    # photo = models.ImageField(upload_to=)
    phone = models.CharField(max_length=10)
    addressline = models.CharField(max_length=120)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES.choices)

#1 -> M
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    caption = models.CharField(max_length=250)
    likes =  models.ManyToManyField(User,through="Like")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#1 -> M
#M -> 1
# M -> M
# junction table needed
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



