# Generated by Django 5.0.2 on 2024-02-14 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_register_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_customer',
            name='arrival_date',
        ),
    ]
