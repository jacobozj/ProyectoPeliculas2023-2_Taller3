# Generated by Django 4.2.5 on 2023-09-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_description_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='movie/images/default.jpg', upload_to='movie/images/'),
        ),
    ]
