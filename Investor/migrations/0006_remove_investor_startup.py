# Generated by Django 3.2.3 on 2021-05-31 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Investor', '0005_alter_company_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='startup',
        ),
    ]
