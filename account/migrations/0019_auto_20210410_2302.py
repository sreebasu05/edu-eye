# Generated by Django 3.1 on 2021-04-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_unit_ideallecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='class_no',
            field=models.IntegerField(),
        ),
    ]