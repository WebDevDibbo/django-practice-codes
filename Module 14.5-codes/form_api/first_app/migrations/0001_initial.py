# Generated by Django 5.0.6 on 2024-06-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=200)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='')),
                ('float_field', models.FloatField()),
                ('integer_field', models.IntegerField()),
                ('json_field', models.JSONField()),
                ('slug_field', models.SlugField()),
                ('text_field', models.TextField()),
                ('time_field', models.TimeField()),
            ],
        ),
    ]
