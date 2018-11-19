from django.core import mail
from django.test import TestCase, Client
from django.urls import reverse

class Test_Send_Mail(TestCase):
	fixtures = ['task_app_test_data.json']

	def test_email_sent(self):
		"""Chech if email is being sent"""
		# prepare client and login as admin
		client= Client()
		client.login(username="task_db_user", password="1592648t")

		# make form submit

		response=client.post(reverse("send_mail_url"), {
			"from_email": "from@gmail.com",
			"subject": "test email",
			"message": "test email message"
			})

		# check if test email backend catched our email
		msg = mail.outbox[0].message()
		self.assertEqual(msg.get("subject"), "test email")
		self.assertEqual(msg.get("from_email"), u"from@gmail.com")
		self.assertEqual(msg.get_pay_load(), "test email message",)