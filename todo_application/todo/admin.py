from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'due_date', 'is_completed')
    list_filter = ('is_completed', 'priority')
    search_fields = ('title', 'description')