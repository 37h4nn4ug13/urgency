# Generated by Django 3.2.12 on 2022-10-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
