# Generated by Django 4.2 on 2023-05-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_like_car_dislike_like_car_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_extiyotqisimlar',
            name='imag',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
