# Generated by Django 3.0.4 on 2020-04-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20200407_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]