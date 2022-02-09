# Generated by Django 3.2.7 on 2022-02-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecategory',
            name='course_category_image',
            field=models.ImageField(blank=True, null=True, upload_to='store_image/course_category_image/'),
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='course_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]