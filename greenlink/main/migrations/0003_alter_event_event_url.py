# Generated by Django 3.2.7 on 2021-10-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]