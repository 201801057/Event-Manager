# Generated by Django 2.2.2 on 2021-01-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20210110_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantregistration',
            name='eventList',
            field=models.CharField(max_length=255),
        ),
    ]
