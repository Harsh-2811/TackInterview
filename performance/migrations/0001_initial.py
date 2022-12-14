# Generated by Django 4.1.1 on 2022-09-16 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Cost in $')),
                ('revenue', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Revenue in $')),
                ('profit', models.DecimalField(blank=True, decimal_places=3, max_digits=20, verbose_name='Profit in $')),
                ('roi', models.DecimalField(blank=True, decimal_places=3, max_digits=20, verbose_name='ROI in %')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HourlyPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('performance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='performance.performance')),
            ],
        ),
        migrations.CreateModel(
            name='DailyPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('daily_revenue', models.DecimalField(blank=True, decimal_places=3, max_digits=20, verbose_name='Daily Revenue in $')),
                ('performance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='performance.performance')),
            ],
        ),
    ]
