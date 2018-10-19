# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

import datetime

from ..models import Task_Details_Model, Chooses_Date_Model
from ..util import get_current_task, get_specific_date

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def choose_date_add_tasks_show_tasks(request):
	if request.method == 'POST':

		if request.POST.get('choose_date_button') is not None:
			# choose date to see tasks on this date

			data = {}
			errors = {}

			
			# -------------
			chooses_date = request.POST.get('chooses_date', '').strip()
			if not chooses_date:
				errors['chooses_date'] = u'Choose date first!'
			else:
				data['chooses_date'] = chooses_date
			if not errors:
			
				new_date = Chooses_Date_Model(**data)
				new_date.save()
			else:
				return render(request, 'task_list.html', {'errors': errors})


			
			
			# show tasks filtered by chooses date and logged user's
			ch_task = Task_Details_Model.objects.filter(date_of_task_execution=str(new_date), author=str(request.user))

			today_task_list = []

			for i in ch_task:	
				today_task_list.append(i)

				# click on the task and see task's detail
			current_task = get_current_task(request)
			if current_task is not None:
				current_details = Task_Details_Model.objects.filter(title=current_task.title)
	
			else:
				current_details = None

			return render(request, 'task_list.html', {'ch_task': today_task_list, 'current_details': current_details})
		

			# add new task
		elif request.POST.get('send_button') is not None:

			task_list = Task_Details_Model.objects.all()[::-1]

			data = {}
			errors = {}

			data['author'] = request.user
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
				return render(request, 'task_list.html', {'errors': errors})	


		elif request.POST.get('cancel_button') is not None:
			#return render(request, 'task_list.html', {})	
			return HttpResponseRedirect(reverse('choose_date_add_tasks_show_tasks_view_url'))


		else:
			return render(request, 'task_list.html', {})

			#return HttpResponseRedirect(u'%s?status_message=You should choose some date!' %(reverse('choose_date_url')))
	else:
		return render(request, 'task_list.html', {})


'''
def task_list(request):

	task_list = Task_Details_Model.objects.all()[::-1]

	specific_date = [Chooses_Date_Model.objects.filter(name=request.user)][::-1]
	print('ddd - ', specific_date)
	for x in specific_date:
		print('specific_date - ', specific_date )
		print('specific_x - ', x )
	#specific_date = str(get_specific_date(request))
	current_task = get_current_task(request)

	if specific_date:

		specific_task = Task_Details_Model.objects.filter(date_of_task_execution=specific_date[0])
	else:
		specific_task = None


	if current_task is not None:
		current_details = Task_Details_Model.objects.filter(title=current_task.title)
	else:
		current_details = None

	return render(request, 'task_list.html', {'task_list': task_list,
												#'specific_task': specific_task[0][0],
												'current_details': current_details})
'''


