# Generated by Django 5.0.1 on 2024-01-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_profile_sent_emails_alter_profile_sub_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sent_emails',
            new_name='sent_free_emails',
        ),
        migrations.AddField(
            model_name='profile',
            name='sent_prem_emails',
            field=models.IntegerField(default=0),
        ),
    ]
