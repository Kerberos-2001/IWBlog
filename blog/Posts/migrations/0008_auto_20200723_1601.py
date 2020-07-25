# Generated by Django 3.0.8 on 2020-07-23 16:01

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_auto_20200723_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[500, 300], upload_to='thumbnail'),
        ),
    ]