# Generated by Django 4.0.4 on 2022-12-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_pagecontents_social_icon_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontents',
            name='page_name',
            field=models.CharField(default='SplitUnity', max_length=20),
        ),
    ]
