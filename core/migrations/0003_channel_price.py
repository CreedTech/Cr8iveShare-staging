# Generated by Django 4.0.4 on 2022-12-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_comment_comment_alter_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='price',
            field=models.PositiveIntegerField(default=12),
            preserve_default=False,
        ),
    ]