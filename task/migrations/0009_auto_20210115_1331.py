# Generated by Django 3.1.4 on 2021-01-15 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20210115_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getdata',
            name='borders',
        ),
        migrations.RemoveField(
            model_name='getdata',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='getdata',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='getdata',
            name='population',
        ),
        migrations.RemoveField(
            model_name='getdata',
            name='timezone',
        ),
    ]