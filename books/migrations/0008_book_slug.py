# Generated by Django 5.1.2 on 2024-10-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_about_book_uzbek_literature'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
