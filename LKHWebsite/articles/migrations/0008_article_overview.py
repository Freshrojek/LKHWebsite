# Generated by Django 3.2.9 on 2021-12-10 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20211206_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='overview',
            field=models.TextField(default='', max_length=64),
        ),
    ]