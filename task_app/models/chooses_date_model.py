# -*- coding: utf-8 -*-
from django.db import models

class Chooses_Date_Model(models.Model):
	class Meta(object):
		verbose_name = u'Chooses date'
		verbose_name_plural = u'Chooses date'


	chooses_date = models.DateField(
		blank = False,
		verbose_name = u'Chooses date')

	def __str__(self):
		return '%s' %(self.chooses_date)