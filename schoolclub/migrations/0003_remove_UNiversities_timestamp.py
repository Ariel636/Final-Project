# Generated by Django 3.1.1 on 2020-10-07 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolclub', '0002_auto_20201007_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='UNiversities',
            name='timestamp',
        ),
    ]
