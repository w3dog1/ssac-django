# Generated by Django 3.2.6 on 2021-08-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True, verbose_name='소개'),
        ),
    ]
