# Generated by Django 5.1.3 on 2024-11-18 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_rename_subject_id_chapter_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='grade_level',
        ),
        migrations.AddField(
            model_name='chapter',
            name='grade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='academics.grade'),
        ),
    ]
