# Generated by Django 4.0.4 on 2022-04-26 19:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0006_alter_comment_content_alter_post_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatar',
            new_name='Perfil',
        ),
    ]