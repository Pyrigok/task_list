from django.core.management.base import BaseCommand

from task_app.models import Task_Details_Model


class Command(BaseCommand):
	args = '<model_name model_name ...>'
	help = "Prints to console number of task in database."

	def add_arguments(self, parser):
		parser.add_argument('task', type=str)

	def handle(self, *args, **options):
		if 'task' in options:
			self.stdout.write('Number of tasks in DB: %d' % Task_Details_Model.objects.count())
			#return Task_Details_Model.objects.count()