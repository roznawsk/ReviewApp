# Generated by Django 3.1.7 on 2021-02-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='section_name',
            new_name='name',
        ),
    ]
