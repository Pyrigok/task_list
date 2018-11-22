
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.forms import ModelForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _



from ..models import Task_Details_Model

class TaskUpdateView(UpdateView):
	model = Task_Details_Model
	fields = ['title', 'content']
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), _('Task edited!'))

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), _('Editing canceled!')))
		else:
			return super(TaskUpdateView, self).post(request, *args, **kwargs)

	def dispatch(self, *args, **kwargs):
		return super(TaskUpdateView, self).dispatch(*args, **kwargs)


class TaskDeleteView(DeleteView):
	model = Task_Details_Model
	template_name_suffix = '_delete_form'

	def get_success_url(self):
		return u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), _('Task deleted!'))

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' %(reverse('choose_date_add_tasks_show_tasks_view_url'), _('Deleting canceled!')))

		else:
			return super(TaskDeleteView, self).post(request, *args, **kwargs)


