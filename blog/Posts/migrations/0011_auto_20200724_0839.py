# Generated by Django 3.0.8 on 2020-07-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0010_auto_20200723_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
