# Generated by Django 2.1.2 on 2018-10-14 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Competition', '0002_auto_20181008_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='trackId',
        ),
    ]
