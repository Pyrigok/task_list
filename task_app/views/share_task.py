'''
			# add task to recipient's task_list
			data = {}
			data['author'] = user

			data['title'] = entry.title

			data['status'] = entry.status

			data['date_of_task_execution'] = entry.date_of_task_execution

			data['content'] = entry.content

			new_task = Task_Details_Model(**data)
			new_task.save()
'''
			# substract shared task from request.user task_list














#def send_email(request, pk):

# 	# get from_email
# 	from_email = request.user.email
# 	from_name = str(request.user)

# 	# get recipient
# 	# get current user from cookie
# 	cur_user = get_current_user(request)
# 	if cur_user is not None:

# 		# get email from user selected from cookie
# 		selected_user=User.objects.filter(username=cur_user)
# 		for user in selected_user:
# 			recipient_email = user.email

# 		recipient_list = []

# 		# add email of current user
# 		recipient_list.append(recipient_email)

# 	else:

# 		selected_user = None
# 		recipient_email = None


# 	# get letter subject(task title) and message(task content) 
# 	current_task = get_current_task(request)
# 	if current_task is not None:
# 		task_details = Task_Details_Model.objects.filter(title=current_task.title)
# 		for entry in task_details:
# 			subject = entry.title
# 			message = 'Hello.\nDo it please next task!\n\n' + entry.content + '.' + '\nThank you!!!\n\n' + from_name + '\n' + from_email

		


# 	else:
# 		current_details = None
# 		subject = None
# 		message = None

	

# # ---
# 	if request.method=='POST':
# 		#form = SendMail(request.POST)

# 		try:
# 			send_mail(subject, message, from_email, recipient_list)

# 		except Exception:
# 			status_message = u'Some error occured! Try again later!'

# 		else:
# 			status_message = u'Message sent succesfully!'

# 		return render(request, 'send_mail.html', {'users_list': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list, 'status_message': status_message})
# 	else:
# 		return render(request, 'send_mail.html', {'users_list': selected_user, 'subject': subject, 'message': message, 'from_email': from_email, 'recipient_list': recipient_list})

# 	return HttpResponseRedirect(u'%s?status_message=Task sent!' % reverse('send_mail_url'))
	