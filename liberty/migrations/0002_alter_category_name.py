# Generated by Django 5.0.2 on 2024-02-29 01:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
