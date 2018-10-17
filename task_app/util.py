import datetime
def get_current_task(request):

	pk = request.COOKIES.get('current_task')

	if pk:
		from .models import Task_Details_Model
		try:
			# find entry from db with current choose id
			task = Task_Details_Model.objects.get(pk=int(pk))

		except Task_Details_Model.DoesNotExist:
			return None
		else:
			return task
	else:
		return None
'''
# func for context processor's
def get_tasks(request):

	from .models import Task_Details_Model

	cur_task = get_current_task(request)

	tasks = []
	for task in Task_Details_Model.objects.all():
		tasks.append({
			'id': task.id,
			'date_of_task_execution': task.date_of_task_execution,
#			'deadline': task.deadline,
			'content': task.content,
			'task_created_on': task.task_created_on
			})
		return tasks'''


def get_specific_date(request):

	pk = request.COOKIES.get('specific_date')

	if pk:
		return pk
		'''pk=int(pk.split('-')[1])#, int(pk.split('-')[1]), int(pk.split('-')[2]))
		print('new_pk -',pk)
		from .models import Task_Details_Model
		try:
			specific_task = Task_Details_Model.objects.filter(pk=int(pk))
		except Task_Details_Model.DoesNotExist:
			return None
		else:
			return specific_task'''
	else:
		return None