# Generated by Django 2.2.1 on 2019-05-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_text', '0003_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=40)),
                ('pid', models.CharField(max_length=40)),
                ('pname', models.CharField(max_length=40)),
                ('pprice', models.CharField(max_length=40)),
            ],
        ),
    ]