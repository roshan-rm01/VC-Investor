# Generated by Django 3.2.3 on 2021-05-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0002_auto_20210530_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='revenue',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='company',
            name='valuation',
            field=models.DecimalField(decimal_places=1, max_digits=100000),
        ),
    ]
