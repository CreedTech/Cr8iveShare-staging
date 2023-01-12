# Generated by Django 4.0.4 on 2023-01-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_user_social_media_link_1_about_user_social_media_link_1_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='John Doe', max_length=100)),
                ('email', models.EmailField(help_text='example@example.com', max_length=254)),
                ('subject', models.CharField(help_text='Contact subject...', max_length=100)),
                ('message', models.TextField(help_text='My name is...')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('second_email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=30)),
                ('second_phone_number', models.CharField(max_length=30)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ContactInfo',
                'verbose_name_plural': 'ContactInfos',
            },
        ),
    ]