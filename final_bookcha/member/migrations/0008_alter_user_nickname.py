# Generated by Django 3.2.7 on 2021-09-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용 중인 닉네임 입니다!'}, max_length=15, null=True, unique=True),
        ),
    ]
