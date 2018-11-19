from django.test import TestCase, Client, override_settings
from django.urls import reverse

from task_app.models import Task_Details_Model

# for english language on the page
@override_settings(LANGUAGE_CODE="en")
class TestEditTask(TestCase):
	fixtures = ["task_app_test_data.json"]

	def setUp(self):
		# remember test browser
		self.client = Client()

		# remember url to edit form
		self.url = reverse("edit_task_url", kwargs={"pk": 1})

	def test_view(self):
		print("'test_view' running")
		# login as admin to access task edit form
		self.client.login(username="task_db_user", password="1592648t")

			# get form and check few fields

		response = self.client.get(self.url)

		# check response status
		self.assertEqual(response.status_code, 200)

		# check page title, few fields and button 
		self.assertIn(b"Editing Page", response.content)
		self.assertIn(b"title", response.content)
		self.assertIn(b"content", response.content)
		self.assertIn(b'Update', response.content)
		self.assertIn(b'Cancel', response.content)
		self.assertIn(b"action='%s'" % self.url, response.content)


	# test 'POST' request
	def test_success(self):
		print('"test_success" running')
		# login as admin
		self.client.login(username="task_db_user", password="1592648t")

		# post form with valid data
		response = self.client.post(self.url, {"title": "Updated title",
											"who_execute": "Updated who_execute",
											"task_created_on": "2018-11-03",
											"date_of_task_execution": "2018-11-03",
											"content": "Updated content"}, follow=True)

		# check response status
		print(self.url)
		print(response.content)
		#self.assertEqual(response.status_code, 200)

		# test updated task details
		task=Task_Details_Model.objects.get(pk=1)
		self.assertEqual(task.title, 'Updated title')
		self.assertEqual(task.who_execute, 'Updated who_execute')
		self.assertEqual(task.date_of_task_execution, '2018-11-03')
		self.assertEqual(task.task_created_on, '2018-11-03')
		self.assertEqual(task.content, 'Updated content')

		# check proper redirect after form post
		self.assertIn("Task edited!", response.content)
		self.assertEqual(response.redirect_chain[0][0],
			'http://testserver/?status_message=' + 'Task%20edited!')
		print('end')
