# Generated by Django 2.2 on 2021-11-30 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storiesapp', '0003_mystory_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mystory',
            name='img',
        ),
    ]