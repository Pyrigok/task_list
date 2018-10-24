from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User

from task_project.settings import EMAIL_HOST_USER
from ..models import Task_Details_Model
from ..util import get_current_user, get_current_task

from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required


def send_email(request, pk):

	# get recipient from cookie
	cur_recipient = get_current_user(request)
	selected_user=User.objects.filter(username=cur_recipient)

	# get current task from cookie
	current_task = get_current_task(request)	
	task_details = Task_Details_Model.objects.filter(title=current_task.title)

	# get from_email
	from_email = request.user.email
	from_name = str(request.user)



	# get email from user selected from cookie
	for user in selected_user:
		recipient_email = user.email

	recipient_list = []

	# add email of current user
	recipient_list.append(recipient_email)



	# get letter subject(task title) and message(task content) 
	
	for entry in task_details:
		subject = entry.title
		message = 'Hello.\nComplete please '+ str(entry.date_of_task_execution) +' next task:\n\n' + entry.content + '.' + '\nThank you!!!\n\n' + from_name + '\n' + from_email

	if request.method=='POST':

		

		try:
			send_mail(subject, message, from_email, recipient_list)

		except Exception:
			status_message = u'Some error occured! Try again later!'

		else:
			status_message = u'Message sent succesfully!'

		# add task to recipient's task_list
		data = {}

		data['from_user'] = str(request.user)

		data['who_execute'] = cur_recipient

		data['title'] = entry.title

		data['status'] = entry.status

		data['date_of_task_execution'] = entry.date_of_task_execution

		data['content'] = entry.content

		new_task = Task_Details_Model(**data)
		new_task.save()

		# substract shared task from request.user task_list
		Task_Details_Model.objects.filter(who_execute=str(request.user), title=entry.title).delete()


		

		return render(request, 'send_mail.html', {'selected_user': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list, 'status_message': status_message})
	else:
		return render(request, 'send_mail.html', {'selected_user': selected_user,  'subject': subject})
		#return render(request, 'send_mail.html', {'users_list': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list})

	return HttpResponseRedirect(u'%s?status_message=Task sent!' % reverse('send_mail_url'))
		# ex_message = u'Canceled!'
		# return HttpResponseRedirect(
		# 	u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), ex_message))

