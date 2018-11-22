# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Task_Details_Model(models.Model):
	class Meta(object):
		verbose_name = _(u'Task description')
		verbose_name_plural = _(u'Tasks description')

	who_execute = models.CharField(
		max_length = 50,
		blank = False,
		verbose_name = _(u'Who execute the task'))

	from_user = models.CharField(
		max_length = 50,
		blank = True,
		
		verbose_name = _(u'From whom task shared'))


	title = models.CharField(
		max_length = 20,
		blank = False,
		verbose_name = _(u'Task title'))

	"""deadline = models.DateField(
		blank = False,
		verbose_name = u'Deadline date')"""

	date_of_task_execution = models.DateField(
		blank = False,
		verbose_name=_(u'Date of task execution'))

	"""priority = models.CharField(
		max_length = 7,
		blank = False,
		verbose_name=u"Task priority")"""

	status = models.CharField(
		max_length = 20,
		blank = True,
		default = 'In the process',
		verbose_name=_(u'Status of task'))

	content = models.CharField(
		max_length=50,
		blank=False,
		verbose_name=_(u'Task description'))

	task_created_on = models.DateField(
		auto_now_add = True,
		verbose_name = _(u'Date of add task'))

	def __str__(self):
		return '%s %s %s %s %s %s %s' %(self.who_execute, self.from_user, self.title, self.date_of_task_execution, self.status, self.content, self.task_created_on)