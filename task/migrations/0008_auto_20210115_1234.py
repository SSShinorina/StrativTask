# Generated by Django 3.1.4 on 2021-01-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20210105_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getdata',
            name='borders',
        ),
        migrations.AddField(
            model_name='getdata',
            name='borders',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='getdata',
            name='languages',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
