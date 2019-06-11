# Generated by Django 2.2.1 on 2019-06-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_text', '0009_auto_20190529_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]