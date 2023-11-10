# Generated by Django 4.2.2 on 2023-10-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('experience', models.CharField(max_length=2)),
                ('rating', models.IntegerField(max_length=2)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('budget', models.CharField(max_length=255)),
                ('no_of_people', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventSavvy.client')),
                ('organiser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventSavvy.organiser')),
            ],
        ),
    ]