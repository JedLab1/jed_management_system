# Generated by Django 5.1.3 on 2024-11-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='chapter_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='chapter_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='subject',
            new_name='subject_id',
        ),
        migrations.RenameField(
            model_name='method',
            old_name='chapter',
            new_name='chapter_id',
        ),
        migrations.RenameField(
            model_name='method',
            old_name='method_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='method',
            old_name='method_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_name',
            new_name='name',
        ),
    ]
