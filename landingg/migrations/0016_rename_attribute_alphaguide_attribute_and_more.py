# Generated by Django 4.1 on 2022-08-29 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingg', '0015_alter_alphaguide_attribute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alphaguide',
            old_name='Attribute',
            new_name='attribute',
        ),
        migrations.RenameField(
            model_name='alphaguide',
            old_name='Letter_Position',
            new_name='letter_Position',
        ),
    ]
