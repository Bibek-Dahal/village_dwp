# Generated by Django 4.0.5 on 2022-06-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwp', '0007_remove_meterreading_is_paid_bill_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
