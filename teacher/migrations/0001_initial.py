# Generated by Django 5.0.7 on 2024-07-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('education_level', models.CharField(max_length=100)),
                ('subject_specialization', models.CharField(max_length=100)),
                ('bank_account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
