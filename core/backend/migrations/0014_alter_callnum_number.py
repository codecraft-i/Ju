# Generated by Django 5.1.6 on 2025-03-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_callnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callnum',
            name='number',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
