# Generated by Django 3.1 on 2021-04-09 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_hod', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BatchCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_no', models.IntegerField()),
                ('name', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.course')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('department', models.IntegerField(choices=[(1, 'Computer Science and Engineering'), (2, 'Electronics and Communications Engineering'), (3, 'Electrical Engineering'), (4, 'Mechanical Engineering')], default=1)),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherBatchCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchcourse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.batchcourse')),
                ('teacher_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.teacherprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('department', models.IntegerField(choices=[(1, 'Computer Science and Engineering'), (2, 'Electronics and Communications Engineering'), (3, 'Electrical Engineering'), (4, 'Mechanical Engineering')], default=1)),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.teacherprofile')),
            ],
        ),
        migrations.AddField(
            model_name='batchcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.course'),
        ),
        migrations.AddField(
            model_name='batch',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.session'),
        ),
        migrations.CreateModel(
            name='TrackProgressCourseBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('batchcourse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.batchcourse')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.unit')),
            ],
            options={
                'unique_together': {('unit', 'batchcourse')},
            },
        ),
    ]
