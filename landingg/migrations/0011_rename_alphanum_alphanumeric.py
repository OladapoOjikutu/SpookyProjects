# Generated by Django 4.1 on 2022-08-25 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingg', '0010_rename_alphanumeric_alphanum'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alphanum',
            new_name='Alphanumeric',
        ),
    ]
