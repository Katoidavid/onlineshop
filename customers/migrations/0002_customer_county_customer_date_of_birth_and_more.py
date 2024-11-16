# Generated by Django 5.0.7 on 2024-11-16 08:39

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='county',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Nakuru', 'Nakuru'), ('Eldoret', 'Eldoret'), ('Thika', 'Thika'), ('Nyeri', 'Nyeri'), ('Machakos', 'Machakos'), ('Meru', 'Meru')], default='Nairobi', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
