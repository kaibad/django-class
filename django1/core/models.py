from django.db import models

# Create your tests here.
class Note(models.Model):
    title = models.CharField(max_length=150)
    desciption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)