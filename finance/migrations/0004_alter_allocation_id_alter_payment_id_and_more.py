# Generated by Django 4.1 on 2022-08-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20211220_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paymentallocation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
