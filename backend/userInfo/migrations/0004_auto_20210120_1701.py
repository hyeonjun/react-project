# Generated by Django 3.1.5 on 2021-01-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0003_auto_20210120_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='profile/image/basic.jpg', upload_to='profile/image/'),
        ),
    ]
