# Generated by Django 5.0.6 on 2024-07-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=11)),
                ('Instrument_type', models.CharField(choices=[('piano', 'Piano'), ('guitar', 'Guitar'), ('drum set', 'Drum set'), ('wind', 'Wind')], max_length=100)),
            ],
        ),
    ]
