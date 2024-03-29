# Generated by Django 3.2.3 on 2021-05-29 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('founder', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250)),
                ('sector', models.CharField(choices=[('entertainment', 'Entertainment'), ('fintech', 'Fintech'), ('enterprise', 'Enterprise'), ('healthcare', 'Healthcare'), ('robotics', 'Robotics')], max_length=100)),
                ('stage', models.CharField(choices=[('series a', 'Series A'), ('series b', 'Series B'), ('series c', 'Series C'), ('series d', 'Series D')], max_length=100)),
                ('description', models.TextField()),
                ('launch_year', models.IntegerField()),
                ('valuation', models.DecimalField(decimal_places=1, max_digits=100)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('personal_opinion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('firm', models.CharField(blank=True, max_length=100)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_pick', to='Investor.company')),
            ],
        ),
    ]
