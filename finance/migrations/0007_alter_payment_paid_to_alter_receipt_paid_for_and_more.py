# Generated by Django 4.1 on 2022-10-14 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0011_rename_state_student_region'),
        ('finance', '0006_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_to',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='paid_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finance.allocation'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis.student'),
        ),
    ]