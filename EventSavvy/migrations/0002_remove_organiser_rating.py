# Generated by Django 4.2.2 on 2023-10-04 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventSavvy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organiser',
            name='rating',
        ),
    ]
