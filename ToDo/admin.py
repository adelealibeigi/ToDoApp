from django.contrib import admin

from .models import *
# Register your models here.


# admin.site.register(TaskList)
@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'priority')
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

