# Generated by Django 3.0.3 on 2020-02-19 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_invoice_generated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]