# Generated by Django 4.0.4 on 2023-01-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialHandle',
        ),
    ]
