"""task_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url

from django.views.generic.base import RedirectView

#from task_app.views.task_list_view import task_list
from task_app.views.task_list_view import choose_date_add_tasks_show_tasks#, TaskUpdateView
from task_app.views.edit_task_view import TaskUpdateView, TaskDeleteView

#from task_app.views.edit_task_view import TaskUpdateView, TaskDeleteView


urlpatterns = [

	#url('/', include('task_app.urls')),
    path('', choose_date_add_tasks_show_tasks, name='choose_date_add_tasks_show_tasks_view_url'),

    # for task's editing
    path('task-edit/<int:pk>', TaskUpdateView.as_view(template_name='edit_task.html'), name='edit_task_url'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(template_name='delete_task.html'), name='delete_task_url'),

    # for django-allauth
    path('accounts/', include('allauth.urls')),



    # django-registration-redux
 #   path('users/', include('users.urls')),
   # url(r'^choose_date/', choose_date_view, name='choose_date_url'),

   # url(r'^$/(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='edit_task_url'),
    #url(r'^$/(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='delete_task_url'),

    path('admin/', admin.site.urls),
]
