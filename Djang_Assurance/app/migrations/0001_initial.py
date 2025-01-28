# Generated by Django 5.1.5 on 2025-01-28 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(130)])),
                ('sex', models.CharField(choices=[('female', 'Femme'), ('male', 'Homme')], default='female', max_length=6)),
                ('weight', models.FloatField(default=60, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)])),
                ('size', models.FloatField(default=170, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(300)])),
                ('children', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('smoker', models.CharField(choices=[('yes', 'Oui'), ('no', 'Non')], default='no', max_length=3)),
                ('region', models.CharField(choices=[('southeast', 'Sud Est'), ('southwest', 'Sud Ouest'), ('northeast', 'Nord Est'), ('northwest', 'Nord Ouest')], default='northwest', max_length=9)),
                ('result', models.FloatField(null=True)),
                ('made_by_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reg_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The name of the regression model (e.g., 'Lasso Regression Model').", max_length=200)),
                ('path', models.FilePathField(help_text='The path to the serialized regression model file.', path='app/regression/models/')),
            ],
        ),
    ]
