# Generated by Django 3.2.5 on 2021-08-14 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210814_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='tilte',
        ),
    ]
