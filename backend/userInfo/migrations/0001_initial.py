# Generated by Django 3.1.5 on 2021-01-20 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=200, unique=True)),
                ('photo', models.ImageField(default='profile/image/basic.jpg', upload_to='profile/image')),
                ('point', models.IntegerField(blank=True, default='0')),
                ('grade', models.IntegerField(blank=True, default='0')),
                ('myIntro', models.CharField(blank=True, max_length=200)),
                ('Tier', models.CharField(blank=True, max_length=20)),
                ('username_info', models.CharField(default='', max_length=150, unique=True)),
                ('email_info', models.EmailField(default='', max_length=254, unique=True)),
                ('password_info', models.CharField(default='', max_length=128)),
                ('name', models.CharField(default='', max_length=150)),
                ('number', models.CharField(default='010', max_length=12, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
