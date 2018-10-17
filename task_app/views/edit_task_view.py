from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from .. models import Task_Details_Model
'''
class TaskUpdateForm(ModelForm):
	class Meta:
		model = Task_Details_Model
		fields = ('title', 'content', 'deadline')

	def __init__(self, *args, **kwargs):
		super(TaskUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_action = reverse('edit_task_url', kwargs={'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		self.helper.layout[-1] = FormActions(
            Submit('save_button', u'Save', css_class="btn btn-primary"),
            Submit('cancel_button', u'Cancel', css_class="btn btn-link"),
        )

class TaskUpdateView(UpdateView):
	model = Task_Details_Model
	template_name = 'task_list.html'
	form_class = TaskUpdateForm

	def get_success_url(self):
		return u'%s?status_message=Task updated!' % reverse('task_list')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Update canceled!' %(reverse('task_list')))
		else:
			return super(TaskUpdateView, self).post(requset, *args, **kwargs)

'''

class TaskDeleteForm(ModelForm):
	class Meta:
		model = Task_Details_Model
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(TaskDeleteteForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_action = reverse('delete_task_url',
			kwargs={'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horisontal'

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-xs-2 control-label'
		self.helper.field_class = 'col-xs-12'

		self.helper.layout[-1] = FormActions(
			Submit('delete_button', u'Delete', css_class='btn btn-danger'),
			Submit('cancel_button', u'Cancel', css_class='btn btn-default'),
		)

class TaskDeleteView(DeleteView):
	model = Task_Details_Model
	template_name = 'task_list.html'

	def get_success_url(self):
		return u'%s?status_message=Task deleted!' %reverse('task_list_url')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Deleting canceled!' %(reverse('task_list_url')))

		else:
			return super(TaskDeleteView, self).post(request, *args, **kwargs)


