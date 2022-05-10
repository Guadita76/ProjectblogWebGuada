# Generated by Django 4.0.4 on 2022-05-04 16:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0021_alter_avatar_image_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(null=True, upload_to='avatares'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]