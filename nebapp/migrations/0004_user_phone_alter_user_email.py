# Generated by Django 4.0.5 on 2022-06-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebapp', '0003_business_image_business_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
