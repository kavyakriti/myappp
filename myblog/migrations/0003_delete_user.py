# Generated by Django 3.0.4 on 2020-03-23 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_news_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
