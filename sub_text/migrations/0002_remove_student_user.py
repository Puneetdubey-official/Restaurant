# Generated by Django 2.2.1 on 2019-05-27 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_text', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
