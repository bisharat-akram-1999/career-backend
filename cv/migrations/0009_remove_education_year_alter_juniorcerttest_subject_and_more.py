# Generated by Django 4.1.3 on 2023-05-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_alter_experience_enddate_alter_experience_startdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='year',
        ),
        migrations.AlterField(
            model_name='juniorcerttest',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='leavingcerttest',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]