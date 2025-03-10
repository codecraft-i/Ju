# Generated by Django 5.1.6 on 2025-03-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_callnum_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaxImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Desktop Surat',
                'verbose_name_plural': 'Desktop Suratlar',
            },
        ),
        migrations.CreateModel(
            name='MinImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Telefon Surat',
                'verbose_name_plural': 'Telefon Suratlar',
            },
        ),
    ]
