# Generated by Django 4.0.4 on 2022-05-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0026_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', null=True, upload_to='posts'),
        ),
    ]
