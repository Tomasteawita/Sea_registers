# Generated by Django 4.2.1 on 2023-06-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
