# Generated by Django 4.2.2 on 2023-10-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventSavvy', '0002_remove_organiser_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='password',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
