# Generated by Django 4.0.4 on 2022-05-05 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0024_alter_avatar_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='avatar',
        ),
    ]