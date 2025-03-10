# Generated by Django 5.1.6 on 2025-03-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_contact_language_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IELTS', models.BooleanField(default=False)),
                ('TOPIK', models.BooleanField(default=False)),
                ('SAT', models.BooleanField(default=False)),
                ('TOEFL', models.BooleanField(default=False)),
                ('PTE', models.BooleanField(default=False)),
                ('GRE', models.BooleanField(default=False)),
                ('GMAT', models.BooleanField(default=False)),
                ('Duolingo', models.BooleanField(default=False)),
                ('KLAT', models.BooleanField(default=False)),
                ('KIIP', models.BooleanField(default=False)),
                ('EPS_TOPIK', models.BooleanField(default=False)),
            ],
        ),
    ]
