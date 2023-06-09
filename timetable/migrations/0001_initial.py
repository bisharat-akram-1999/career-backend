# Generated by Django 4.1.3 on 2023-04-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.TimeField(null=True)),
                ('endslot', models.TimeField(null=True)),
                ('day', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1)),
                ('year', models.PositiveSmallIntegerField()),
                ('week', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
