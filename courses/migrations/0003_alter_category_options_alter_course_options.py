# Generated by Django 4.1 on 2022-08-21 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_tag_lesson_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['subject']},
        ),
    ]