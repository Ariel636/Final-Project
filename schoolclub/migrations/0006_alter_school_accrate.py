# Generated by Django 3.2.9 on 2022-02-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolclub', '0005_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='accrate',
            field=models.CharField(blank=True, choices=[('3.0-3.9%', '3.0-3.9%'), ('4.0-4.9%', '4.0-4.9%'), ('5.0-5.9%', '5.0-5.9%'), ('6.0-6.9%', '6.0-6.9%'), ('7.0-7.9%', '7.0-7.9%'), ('8.0-8.9%', '8.0-8.9%'), ('9.0-9.9%', '9.0-9.9%')], default='Select accrate', max_length=64),
        ),
    ]