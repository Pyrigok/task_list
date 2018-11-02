import datetime

# Client - for make request to the view we need
from django.test import TestCase, Client
from django.urls import reverse

from task_app.models import Task_Details_Model

class TestTaskList(TestCase):

	def setUp(self):
		task2, created = Task_Details_Model.objects.get_or_create(
			id=2,
			title='TASK2',
			who_execute='USER2',
			date_of_task_execution=datetime.datetime.today(),
			content = 'CONTENT2'
			)
		
		task3, created = Task_Details_Model.objects.get_or_create(
			id=3,
			title='TASK3',
			who_execute='USER3',
			date_of_task_execution=datetime.datetime.today(),
			content = 'CONTENT2'
			)

		# remember test browser
		self.client = Client()

		# rememder url to task_list page
		self.url = reverse('choose_date_add_tasks_show_tasks_view_url')


	def test_get_tasks_fitered_by_selected_date(self):
		# set today_date as currently selected date
		s_date = Task_Details_Model.objects.filter(date_of_task_execution=datetime.datetime.today())[0]
		self.client.cookies['selected_date'] = s_date.id

		# make request to the server to get task_list page
		response = self.client.get(self.url)

		# today we have 2 tasks
		print(response.context)
		self.assertEqual(len(response.context['today_task_list']), 2)




	def test_choose_date_add_tasks_show_tasks(self):

		# make request to the server to get task_list page
		response = self.client.get(self.url)
		print('content -', response.content)

		# have we received OK status from the server?
		self.assertEqual(response.status_code, 200)

		# do we have task title on a page?
		self.assertIn('TASK2', response.content)

		# do we have link to task edit page?
		self.assertIn(reverse('task_edit_url', 
				kwargs={'pk': Task_Details_Model.objects.all()[0].id}),
				response.content)

		# do we have link to task delete page?
		self.assertIn(reverse('task_delete_url', 
				kwargs={'pk': Task_Details_Model.objects.all()[0].id}),
				response.content)

		# do we have link to send mail page?
		self.assertIn(reverse('send_mail_url', 
				kwargs={'pk': Task_Details_Model.objects.all()[0].id}),
				response.content)

