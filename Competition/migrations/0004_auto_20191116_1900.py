# Generated by Django 2.2.7 on 2019-11-16 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Competition', '0003_remove_results_trackid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='current_record',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracks',
            name='length',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]