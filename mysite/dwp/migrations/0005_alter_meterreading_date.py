# Generated by Django 4.0.5 on 2022-06-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwp', '0004_alter_bill_extra_fees_alter_bill_late_fine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreading',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
