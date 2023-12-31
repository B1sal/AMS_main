# Generated by Django 4.2.2 on 2023-07-13 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Students',
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('primary_number', models.CharField(max_length=10, null=True, unique=True)),
                ('secondary_number', models.CharField(max_length=10, null=True, unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('my_image', models.ImageField(null=True, upload_to='profile_img/')),
                ('is_student', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Person',
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('shift', models.CharField(choices=[('M', 'Morning'), ('D', 'Day')], max_length=1)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.person')),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'db_table': 'Course',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.student')),
            ],
            options={
                'verbose_name_plural': 'Classes',
                'db_table': 'Class',
            },
        ),
    ]
