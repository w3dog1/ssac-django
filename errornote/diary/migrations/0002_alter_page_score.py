# Generated by Django 3.2.7 on 2021-09-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='score',
            field=models.IntegerField(),
        ),
    ]
