from django.contrib import admin

# Register your models here.
from . import models

class TodoAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'date_created', 'is_completed']
    search_fields = ['title', 'body']
    list_filter = ['date_created', 'is_completed']
    list_display = ['title', 'body', 'is_completed', 'date_created']
    list_editable = ['is_completed']

admin.site.register(models.Todo, TodoAdmin)
# admin.site.register(TodoAdmin)