# Generated by Django 3.2.7 on 2022-02-28 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_otprequest_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
