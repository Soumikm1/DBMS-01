# Generated by Django 5.0.2 on 2024-03-03 23:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festapp', '0012_remove_event_winning_user_remove_organizer_event_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organizers',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='organized_events',
        ),
        migrations.AddField(
            model_name='event',
            name='winning_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organizer',
            name='event',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizer', related_query_name='organizer', to='festapp.event'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winners', to='festapp.event'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='won_positions', to=settings.AUTH_USER_MODEL),
        ),
    ]
