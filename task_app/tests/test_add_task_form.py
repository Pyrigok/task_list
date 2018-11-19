from django.test import TestCase, Client, override_settings

from django.urls import reverse
import datetime
from django.utils import timezone

from task_app.models import Task_Details_Model

# for english language on the page
@override_settings(LANGUAGE_CODE="en")
class TestAddTaskForm(TestCase):

	fixtures = ['task_app_test_data.json']
	def setUp(self):
		self.client = Client()
		self.url = reverse("choose_date_add_tasks_show_tasks_view_url")

	def test_title_fields_button(self):
		response = self.client.get(self.url)
		#self.assertIn(b"New Task", response.content)
		self.assertIn(b"Add task", response.content)
		self.assertIn(b"Close", response.content)
		self.assertIn(b"title", response.content)

		