# Generated by Django 5.0.2 on 2024-03-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festapp', '0016_remove_event_event_organizer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
