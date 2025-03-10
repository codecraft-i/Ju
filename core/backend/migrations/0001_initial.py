# Generated by Django 5.1.6 on 2025-03-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('request_count', models.IntegerField(default=1)),
                ('last_request', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'IP Address',
                'verbose_name_plural': 'IP Address',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_checked', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3)),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontaktlar',
            },
        ),
        migrations.CreateModel(
            name='CheckedContact',
            fields=[
            ],
            options={
                'verbose_name': 'Tekshirilgan Kontakt',
                'verbose_name_plural': 'Tekshitilgan Kontaklar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('backend.contact',),
        ),
        migrations.CreateModel(
            name='UncheckedContact',
            fields=[
            ],
            options={
                'verbose_name': 'Tekshirilmagan Kontakt',
                'verbose_name_plural': 'Tekshirilmagan Kontaklar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('backend.contact',),
        ),
    ]
