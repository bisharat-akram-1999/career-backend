# Generated by Django 4.1.3 on 2023-04-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proffession', models.CharField(max_length=50)),
                ('goal', models.CharField(max_length=50)),
                ('actions', models.CharField(max_length=200)),
                ('realistic', models.BooleanField(default=False)),
                ('countdown', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
