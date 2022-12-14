# Generated by Django 3.2.12 on 2022-10-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=240)),
                ('due', models.DateField(blank=True)),
                ('due_time', models.TimeField(blank=True)),
                ('progress', models.IntegerField(default=0)),
                ('red', models.IntegerField(default=255)),
                ('green', models.IntegerField(default=255)),
                ('blue', models.IntegerField(default=255)),
            ],
        ),
    ]
