# Generated by Django 4.1 on 2023-02-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfsg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]