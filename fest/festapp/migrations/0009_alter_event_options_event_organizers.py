# Generated by Django 5.0.2 on 2024-03-03 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festapp', '0008_winner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='festapp.organizer'),
        ),
    ]
