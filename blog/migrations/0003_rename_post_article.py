# Generated by Django 4.1.2 on 2022-10-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]
