from django.contrib import admin

from .models import Task_Details_Model

class Task_Details_Model_Admin(admin.ModelAdmin):
	list_display = ['title', 'task_created_on', 'date_of_task_execution', 'status', 'who_execute', 'from_user']
	ordering = ['task_created_on', 'date_of_task_execution', 'status', 'who_execute', 'from_user']

admin.site.register (Task_Details_Model, Task_Details_Model_Admin)