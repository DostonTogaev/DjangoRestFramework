# Generated by Django 5.0.7 on 2024-08-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_category_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]