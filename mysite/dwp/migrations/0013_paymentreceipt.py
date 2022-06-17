# Generated by Django 4.0.5 on 2022-06-17 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dwp', '0012_remove_employee_type_employee_type_of_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_amount', models.PositiveSmallIntegerField(verbose_name='received_amount')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dwp.employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'payment receipt',
                'verbose_name_plural': 'payment receipts',
            },
        ),
    ]