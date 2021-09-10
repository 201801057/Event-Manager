# Generated by Django 2.2.2 on 2021-01-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('posterLink', models.URLField()),
                ('eventFrom', models.DateField()),
                ('eventTo', models.DateField()),
                ('eventDeadline', models.DateField()),
                ('hostID', models.EmailField(max_length=254)),
            ],
        ),
    ]