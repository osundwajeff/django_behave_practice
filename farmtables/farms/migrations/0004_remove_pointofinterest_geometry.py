# Generated by Django 4.2.3 on 2023-08-06 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_alter_condition_image_alter_pointofinterest_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='geometry',
        ),
    ]
