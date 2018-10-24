import datetime

from django.test import TestCase
from django.http import HttpRequest

from task_app.models import Task_Details_Model
from task_app.util import get_current_task, get_selected_date

class UtilsTestCase(TestCase):
	"""Test functions from util module"""

	def setUp(self):
		# create set of data in database
		task1, created = Task_Details_Model.objects.get_or_create(
			id=1,
			title='TASK1',
			who_execute='USER1',
			date_of_task_execution=datetime.datetime.today(),
			content = 'CONTENT1'
			)


	def test_get_current_task(self):
		# prepare request object to pass to utility function
		request = HttpRequest()

		# test with no task in cookie
		request.COOKIES['current_task'] = ''
		self.assertEqual(None, get_current_task(request))

		#test with invalid task id
		request.COOKIES['current_task'] = '12345'
		self.assertEqual(None, get_current_task(request))

		# test with valid task id
		task = Task_Details_Model.objects.filter(title='TASK1')[0]
		request.COOKIES['current_task'] = str(task.id)
		self.assertEqual(task, get_current_task(request))


	def test_get_current_date(self):
		request = HttpRequest()

		request.COOKIES['selected_date'] = ''
		self.assertEqual(None, get_selected_date(request))

		request.COOKIES['selected_date'] = '123123'
		self.assertEqual(None, get_selected_date(request))

		sel_date = Task_Details_Model.objects.filter(date_of_task_execution=datetime.datetime.today())[0]
		request.COOKIES['selected_date'] = str(sel_date.id)
		self.assertEqual(sel_date, get_selected_date(request))