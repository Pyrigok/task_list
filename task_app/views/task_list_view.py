# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

import datetime

from django.contrib.auth.models import User


from ..models import Task_Details_Model
from ..util import get_current_task, get_selected_date

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def choose_date_add_tasks_show_tasks(request):

		# show dates for which the user has a task
	filtered_task_by_request_user = Task_Details_Model.objects.filter(who_execute=str(request.user)).order_by('date_of_task_execution')
	

		# click on date and see task list on this date
	selected_date_entry_from_cookie = get_selected_date(request)
	if selected_date_entry_from_cookie is not None:
		selected_data_list = [selected_date_entry_from_cookie]

		for entry in selected_data_list:
			selected_date_with_task = entry.date_of_task_execution

		today_task_list = Task_Details_Model.objects.filter(date_of_task_execution=selected_date_with_task, who_execute=str(request.user))
	else:
		today_task_list = None


		# click on the task and see task's detail
	current_task = get_current_task(request)
	if current_task is not None:
		current_details = Task_Details_Model.objects.filter(title=current_task.title)
		users_list = User.objects.all()


	else:
		current_details = None
		users_list = None


		# add new task
	if request.method == 'POST':

		if request.POST.get('send_button') is not None:

			task_list = Task_Details_Model.objects.all()[::-1]

			data = {}
			errors = {}

			data['who_execute'] = request.user
			data['status'] = 'In the process'

			title = request.POST.get('title', '').strip()
			if not title:
				errors['title'] = u'Fill this field!'
			else:
				data['title'] = title

			date_of_task_execution = request.POST.get('date_of_task_execution', '').strip()
			if not date_of_task_execution:
				errors['date_of_task_execution'] = u'Fill this field'
			else:
				date_of_task_exec = datetime.date(int(date_of_task_execution.split('-')[0]),
						int(date_of_task_execution.split('-')[1]),
						int(date_of_task_execution.split('-')[2]))

				current_date = datetime.date.today()
				difference = str(date_of_task_exec - current_date).split()[0]

				if (str(date_of_task_exec) == str(current_date)) or int(difference) > 0:
					data['date_of_task_execution'] = date_of_task_execution
				else:
					errors['date_of_task_execution'] = "Choose correct date!"

			content = request.POST.get('content', '').strip()
			if not content:
				errors['content'] = u'Fill this field!'
			else:
				data['content'] = content


			if not errors:
				new_task = Task_Details_Model(**data)
				new_task.save()

				return HttpResponseRedirect('%s?status_message=Task added!' %(reverse('choose_date_add_tasks_show_tasks_view_url')))

			else:
				return render(request, 'task_list.html', {'errors': errors, 'filtered_task_by_request_user': filtered_task_by_request_user, 'today_task_list': today_task_list})	


		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect(reverse('choose_date_add_tasks_show_tasks_view_url'))


		else:
			return render(request, 'task_list.html', {'filtered_task_by_request_user': filtered_task_by_request_user, 'today_task_list': today_task_list})

	else:
		return render(request, 'task_list.html', {'users_list': users_list, 'current_details': current_details, 'filtered_task_by_request_user': filtered_task_by_request_user, 'today_task_list': today_task_list})

