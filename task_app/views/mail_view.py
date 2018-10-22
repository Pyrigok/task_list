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


'''
class SendMail(forms.Form):
	from_email = forms.EmailField(
		label=u'Your Email Address')

	subject = forms.CharField(
		label = u'Letter title')

	message = forms.CharField(
		label = u'Letter content',
		max_length = 2560,
		widget = forms.TextInput)
'''
# for share task we change the task author
			# class TaskShareView(UpdateView):
			# 	model = Task_Details_Model
			# 	fields = ['author']
			# 	template_name_suffix = '_share_form'

			# 	def get_success_url(self):
			# 		return u'%s?status_message=Task shared!' %reverse('choose_date_add_tasks_show_tasks_view_url')

			# 	def post(self, request, *args, **kwargs):
			# 		if request.POST.get('cancel_button'):
			# 			return HttpResponseRedirect(u'%s?status_message=Sharing canceled!' %(reverse('choose_date_add_tasks_show_tasks_view_url')))
			# 		else:
			# 			return super(TaskUpdateView, self).post(request, *args, **kwargs)

			# 	def dispatch(self, *args, **kwargs):
			# 		return super(TaskUpdateView, self).dispatch(*args, **kwargs)


def send_email(request, pk):

	# get from_email
	from_email = request.user.email
	from_name = str(request.user)

	# get recipient
	# get current user from cookie
	cur_user = get_current_user(request)
	if cur_user is not None:

		# get email from user selected from cookie
		selected_user=User.objects.filter(username=cur_user)
		for user in selected_user:
			recipient_email = user.email

		recipient_list = []

		# add email of current user
		recipient_list.append(recipient_email)

	else:

		selected_user = None
		recipient_email = None


	# get letter subject(task title) and message(task content) 
	current_task = get_current_task(request)
	if current_task is not None:
		task_details = Task_Details_Model.objects.filter(title=current_task.title)
		for entry in task_details:
			subject = entry.title
			message = 'Hello.\nDo it please next task!\n\n' + entry.content + '.' + '\nThank you!!!\n\n' + from_name + '\n' + from_email

		


	else:
		current_details = None
		subject = None
		message = None

	

# ---
	if request.method=='POST':
		#form = SendMail(request.POST)

		try:
			send_mail(subject, message, from_email, recipient_list)

		except Exception:
			status_message = u'Some error occured! Try again later!'

		else:
			status_message = u'Message sent succesfully!'

		return render(request, 'send_mail.html', {'users_list': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list, 'status_message': status_message})
	else:
		return render(request, 'send_mail.html', {'users_list': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list})

	return HttpResponseRedirect(u'%s?status_message=Task sent!' % reverse('send_mail_url'))
		# ex_message = u'Canceled!'
		# return HttpResponseRedirect(
		# 	u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), ex_message))


'''
		if form.is_valid():
			subject=form.cleaned_data['subject']
			message = form.cleaned_data['message']
			from_email = form.cleaned_data['from_email']

			try:
				send_mail(subject, message, from_email, recipient_list)

			except Exception:
				message = u'Some error occured! Try again later!'

			else:
				message = u'Message send succesfully!'

			return HttpResponseRedirect(
				u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), message))

	else:
		form = SendMail()
'''
		#return render(request, 'send_mail.html', {'users_list': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list})
	#return render(request, 'send_mail.html', {'users_list': selected_user, 'form': form})


'''
	subject = 'Thank you for registering to our site!'
	message = 'message content'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ['pyrigok@i.ua', 'travel_pr@ukr.net']

	send_mail(subject, message, email_from, recipient_list)

	return redirect('choose_date_add_tasks_show_tasks_view_url')
	return render (request, 'send_mail.html', {})
'''