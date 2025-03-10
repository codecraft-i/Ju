# Generated by Django 5.1.6 on 2025-03-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user_id', models.BigIntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
