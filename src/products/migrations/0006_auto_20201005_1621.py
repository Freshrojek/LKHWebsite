# Generated by Django 3.1.1 on 2020-10-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201001_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
