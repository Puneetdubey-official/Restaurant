# Generated by Django 2.2.1 on 2019-05-27 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('marks', models.IntegerField()),
                ('favorite_fruit', models.CharField(max_length=40)),
                ('countries', models.CharField(max_length=40)),
                ('fruits', models.CharField(max_length=40)),
                ('docfile', models.FileField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]