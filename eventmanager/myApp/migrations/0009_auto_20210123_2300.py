# Generated by Django 2.2.2 on 2021-01-23 17:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20210123_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='eventId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='participantregistration',
            name='pId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
