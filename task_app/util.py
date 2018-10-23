
# func for receive task id from cookie
def get_current_task(request):

	pk = request.COOKIES.get('current_task')

	if pk:
		from .models import Task_Details_Model
		try:
			# find entry from db with current chooses id
			task = Task_Details_Model.objects.get(pk=int(pk))

		except Task_Details_Model.DoesNotExist:
			return None
		else:
			return task
	else:
		return None

# func for receive user id from cookie
def get_current_user(request):

	pk = request.COOKIES.get('recipient')


	if pk:
		from django.contrib.auth.models import User

		try:
			# find user from db with current chooses id
			user = User.objects.get(pk=int(pk))


		except User.DoesNotExist:
			return None
		else:
			return user
	else:
		return None

# for receive date from cookie
def get_selected_date(request):

	pk = request.COOKIES.get('selected_date')

	if pk:
		from .models import Task_Details_Model
		try:
			# find task with selected date
			today_task = Task_Details_Model.objects.get(pk=int(pk))

		except Task_Details_Model.DoesNotExist:
			return None
		else:
			return today_task
	else:
		return None
