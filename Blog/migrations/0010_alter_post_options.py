# Generated by Django 4.0.4 on 2022-04-29 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_alter_post_options_alter_post_image_delete_perfil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
    ]