# Generated by Django 5.0.2 on 2024-03-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festapp', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='event_thumbnails/'),
        ),
    ]
