# Generated by Django 3.1.4 on 2021-01-02 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alphacode2', models.CharField(max_length=255)),
                ('capital', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
                ('timezone', models.DateTimeField()),
                ('flag', models.ImageField(upload_to='')),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='task.language')),
                ('neighbouring_countries', models.ManyToManyField(to='task.Country')),
            ],
        ),
    ]