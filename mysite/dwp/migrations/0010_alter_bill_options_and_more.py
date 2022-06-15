# Generated by Django 4.0.5 on 2022-06-15 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dwp', '0009_rename_date_bill_updated_at_bill_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'verbose_name': 'bill', 'verbose_name_plural': 'bills'},
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='current_reading',
            field=models.PositiveSmallIntegerField(verbose_name='current reading'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='extra_consumption_charge',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='extra consumption charge'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='minimum_charge',
            field=models.PositiveSmallIntegerField(verbose_name='minimum charge'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='previous_reading',
            field=models.PositiveSmallIntegerField(verbose_name='previous reading'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='read_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='read by'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='total',
            field=models.PositiveSmallIntegerField(verbose_name='meter number'),
        ),
        migrations.AlterField(
            model_name='meterreading',
            name='water_meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dwp.watermeter', verbose_name='water meter'),
        ),
    ]
