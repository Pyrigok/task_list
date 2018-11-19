from django.core.management.base import BaseCommand

from task_app.models import Task_Details_Model
from django.contrib.auth.models import User


class Command(BaseCommand):
	args = '<model_name model_name ...>'
	help = "Prints to console number of task in database."

	models = (('task', Task_Details_Model), ('user', User))

	def add_arguments(self, parser):
		parser.add_argument('task', type=str)
		parser.add_argument('user', type=str)

	def handle(self, *args, **options):
		for name, model in self.models:
			if name in options:
				self.stdout.write('Number of %ss in DB: %d' % (name, model.objects.count()))
