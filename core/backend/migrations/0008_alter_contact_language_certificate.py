# Generated by Django 5.1.6 on 2025-03-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_contact_language_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='language_certificate',
            field=models.CharField(choices=[('IELTS', 'IELTS'), ('TOPIK', 'TOPIK'), ('SAT', 'SAT'), ('TOEFL', 'TOEFL'), ('PTE', 'PTE'), ('GRE', 'GRE'), ('GMAT', 'GMAT'), ('Duolingo', 'Duolingo'), ('KLAT', 'KLAT'), ('KIIP', 'KIIP'), ('EPS-TOPIK', 'EPS-TOPIK'), ('No', 'ENDI OLAMAN')], default='No', max_length=11),
        ),
    ]
