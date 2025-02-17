# Generated by Django 5.1.3 on 2024-11-29 17:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_remove_activitymodel_svg_content_activitymodel_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityinstance',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='activityinstance',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='activityinstance',
            name='attempted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
