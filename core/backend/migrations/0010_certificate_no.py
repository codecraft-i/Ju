# Generated by Django 5.1.6 on 2025-03-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='NO',
            field=models.BooleanField(default=False),
        ),
    ]
