# Generated by Django 4.1 on 2022-08-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_image_alter_lesson_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, to='courses.tag'),
        ),
    ]
