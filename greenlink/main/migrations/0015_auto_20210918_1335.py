# Generated by Django 3.2.7 on 2021-09-18 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notice',
            name='member',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notice',
            name='notice_views',
            field=models.IntegerField(default=1),
        ),
    ]
