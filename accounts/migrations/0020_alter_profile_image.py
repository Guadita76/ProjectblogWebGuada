# Generated by Django 4.0.4 on 2022-05-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='batman.png', null=True, upload_to='avatares'),
        ),
    ]