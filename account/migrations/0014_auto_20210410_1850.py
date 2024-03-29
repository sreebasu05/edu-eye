# Generated by Django 3.0.6 on 2021-04-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20210410_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackprogressbatchcourse',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trackprogressbatchcourse',
            name='lecture_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trackprogressbatchcourse',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trackprogressbatchcourse',
            name='students_polled',
            field=models.IntegerField(default=0),
        ),
    ]
