# Generated by Django 2.1.1 on 2018-09-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0004_auto_20180909_1355'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]