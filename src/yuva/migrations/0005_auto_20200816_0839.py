# Generated by Django 2.2.13 on 2020-08-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuva', '0004_auto_20200816_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='doj',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hr',
            name='employee_id',
            field=models.CharField(max_length=50),
        ),
    ]