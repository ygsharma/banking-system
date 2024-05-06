# Generated by Django 4.2.11 on 2024-05-06 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_loan_status_loan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='address',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(choices=[('personal', 'Personal Loan'), ('home', 'Home Loan'), ('education', 'Education Loan')], default='personal', max_length=10),
        ),
    ]