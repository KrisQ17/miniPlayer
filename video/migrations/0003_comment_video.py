# Generated by Django 4.0.1 on 2022-01-22 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_videostat_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='video.video'),
            preserve_default=False,
        ),
    ]
