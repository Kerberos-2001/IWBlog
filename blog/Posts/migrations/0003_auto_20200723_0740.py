# Generated by Django 3.0.8 on 2020-07-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20200723_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
