# Generated by Django 5.0.2 on 2024-02-19 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cinema",
            new_name="Movie",
        ),
    ]