# Generated by Django 2.0 on 2018-10-19 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_details_model',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Author of task'),
            preserve_default=False,
        ),
    ]
