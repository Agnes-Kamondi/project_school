# Generated by Django 5.0.7 on 2024-07-22 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_class', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('syllabus', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('prerequisites', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trimester', models.PositiveSmallIntegerField()),
                ('course_head', models.CharField(max_length=100)),
                ('enrollment_limit', models.IntegerField()),
                ('classes', models.ManyToManyField(related_name='classes', to='student_class.student_class')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher')),
            ],
        ),
    ]
