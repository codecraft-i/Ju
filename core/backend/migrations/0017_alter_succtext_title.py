# Generated by Django 5.1.6 on 2025-03-09 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_succdesc_succdocpic_succlink_succtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='succtext',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
