# Generated by Django 3.2.7 on 2021-09-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_book_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookcovers',
            field=models.ImageField(default='bookcha_logo.png', upload_to='static/'),
        ),
    ]
