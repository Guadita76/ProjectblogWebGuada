# Generated by Django 4.0.4 on 2022-05-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0031_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]