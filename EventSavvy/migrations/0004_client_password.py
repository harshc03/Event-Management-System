# Generated by Django 4.2.2 on 2023-10-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventSavvy', '0003_organiser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
