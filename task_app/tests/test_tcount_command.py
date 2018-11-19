from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO


class TCountTest(TestCase):
	"""Test tcount command"""

	fixtures = ['task_app_test_data.json']

	def test_command_output(self):
		# prepare output file for command
		out = StringIO()

		# call our command
		call_command('tcount', 'user', 'task', stdout=out)

		# get command output
		result = out.getvalue()

		# check if we get proper number of objects in database
		self.assertIn('tasks in DB: 2', result)
		self.assertIn('users in DB: 1', result)