# Generated by Django 4.0.4 on 2022-04-26 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_rename_avatar_perfil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
    ]
