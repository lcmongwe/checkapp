# Generated by Django 4.0.5 on 2022-06-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebapp', '0008_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pics/'),
        ),
    ]