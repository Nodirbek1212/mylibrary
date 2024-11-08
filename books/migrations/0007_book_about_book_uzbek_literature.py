# Generated by Django 5.1.2 on 2024-10-26 05:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='about',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='uzbek_literature',
            field=models.BooleanField(default=True),
        ),
    ]
