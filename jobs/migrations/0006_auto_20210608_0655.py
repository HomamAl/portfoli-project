# Generated by Django 3.2 on 2021-06-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(default='', max_length=1500),
        ),
    ]
