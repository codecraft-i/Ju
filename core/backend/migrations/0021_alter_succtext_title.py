# Generated by Django 5.1.6 on 2025-03-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_alter_succtext_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='succtext',
            name='title',
            field=models.TextField(blank=True, help_text='Agar qatorni tugatguvchi bo‘lsangiz <code>&lt;br&gt;</code> yozing.<br>Agar so‘zni belgilab qo‘ymoqchi bo‘lsangiz <code>&lt;span&gt;</code> ichida yozing.', max_length=500, null=True),
        ),
    ]
