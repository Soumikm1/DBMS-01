# Generated by Django 5.0.2 on 2024-03-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festapp', '0013_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
