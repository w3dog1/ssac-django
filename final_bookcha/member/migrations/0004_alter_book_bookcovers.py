# Generated by Django 3.2.7 on 2021-09-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_book_bookcovers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookcovers',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
