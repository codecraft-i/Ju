# Generated by Django 5.1.6 on 2025-03-09 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_alter_succtext_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='succtext',
            name='title',
            field=models.TextField(blank=True, help_text="Agar qatorni tugatguvchi <br> tegi yozing \nAgar so'zni belgilab qo'ymoqchi bo'lsangiz <span>Belgilangan so'z</span> tegi ichida so'zlarni yozing.", max_length=500, null=True),
        ),
    ]
