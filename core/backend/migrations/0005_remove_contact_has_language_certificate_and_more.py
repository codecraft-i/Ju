# Generated by Django 5.1.6 on 2025-03-07 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_contact_has_language_certificate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='has_language_certificate',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='no_language_certificate',
        ),
    ]
