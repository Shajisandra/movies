# Generated by Django 4.2.2 on 2023-07-31 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
