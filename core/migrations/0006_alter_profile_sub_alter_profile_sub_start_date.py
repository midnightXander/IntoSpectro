# Generated by Django 5.0.1 on 2024-01-24 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_profile_sub_type_alter_profile_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sub',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 21, 23, 0, 957817)),
        ),
    ]
