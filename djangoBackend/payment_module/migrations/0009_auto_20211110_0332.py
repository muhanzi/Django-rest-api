# Generated by Django 3.1.2 on 2021-11-10 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_module', '0008_invoice_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentLink',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transactionId',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
