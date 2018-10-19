from django.contrib import admin

from .models import Task_Details_Model, Chooses_Date_Model

class Task_Details_Model_Admin(admin.ModelAdmin):
	list_display = ['title', 'task_created_on', 'date_of_task_execution', 'status', 'author']
	ordering = ['task_created_on', 'date_of_task_execution', 'status', 'author']

admin.site.register (Task_Details_Model, Task_Details_Model_Admin)
admin.site.register (Chooses_Date_Model)	