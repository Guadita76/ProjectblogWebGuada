# Generated by Django 4.0.4 on 2022-04-24 02:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_rename_profile_avatar_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]