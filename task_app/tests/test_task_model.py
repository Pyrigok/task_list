from django.test import TestCase
from task_app.models import Task_Details_Model

class Test_Task_Model(TestCase):

	def setUp(self):
		pass

	# 'who_execute' column test
	def test_who_execute_verbose_name(self):
		print('test_who_execute_verbose_name running')
		task=Task_Details_Model.objects.get(pk=1)
		field_verbose_name=task._meta.get_field('who_execute').verbose_name
		self.assertEqual(field_verbose_name, 'Who execute the task')

	def test_who_execute_blank(self):
		print('test_who_execute_blank running')
		task=Task_Details_Model.objects.get(pk=1)
		field_blank=Task_Details_Model._meta.get_field('who_execute').blank
		self.assertEqual(field_blank, False)

	def test_who_execute_max_length(self):
		print('test_who_execute_max_length running')
		task=Task_Details_Model.objects.get(pk=1)
		field_max_length=task._meta.get_field('who_execute').max_length
		self.assertEqual(field_max_length, 50)

	# 'from_user' column test
	def test_from_user_max_length(self):
		print('test_from_user_max_length running')
		task=Task_Details_Model.objects.get(pk=1)
		field_max_length = task._meta.get_field('from_user').max_length
		self.assertEqual(field_max_length, 50)

	def test_from_user_verbose_name(self):
		print('test_from_user_verbose_name running')
		task=Task_Details_Model.objects.get(pk=1)
		field_verbose_name=task._meta.get_field('from_user').verbose_name
		self.assertEqual(field_verbose_name, 'From whom task shared')

	

	

