# Generated by Django 2.2.2 on 2021-01-23 16:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_auto_20210110_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='eventId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
