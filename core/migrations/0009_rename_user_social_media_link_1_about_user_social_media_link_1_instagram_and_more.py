# Generated by Django 4.0.4 on 2023-01-10 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_about_user_social_media_1_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='user_social_media_link_1',
            new_name='user_social_media_link_1_instagram',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='user_social_media_link_2',
            new_name='user_social_media_link_2_instagram',
        ),
    ]