# Generated by Django 5.1.3 on 2024-11-18 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('chapter_id', models.AutoField(primary_key=True, serialize=False)),
                ('chapter_name', models.CharField(max_length=255)),
                ('grade_level', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('method_id', models.AutoField(primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.subject'),
        ),
    ]
