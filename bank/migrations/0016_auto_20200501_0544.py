# Generated by Django 2.2.10 on 2020-05-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0015_auto_20200501_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
