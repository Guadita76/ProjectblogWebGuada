# Generated by Django 4.0.4 on 2022-05-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0025_delete_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='wii_fit.png', null=True, upload_to='posts'),
        ),
    ]
