# Generated by Django 3.1.2 on 2021-05-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20210503_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
