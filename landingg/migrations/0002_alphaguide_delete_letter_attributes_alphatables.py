# Generated by Django 4.1 on 2022-08-14 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landingg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlphaGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Letter_Position', models.CharField(max_length=30)),
                ('Attribute', models.TextField(max_length=700)),
            ],
        ),
        migrations.DeleteModel(
            name='letter_Attributes',
        ),
        migrations.CreateModel(
            name='Alphatables',
            fields=[
                ('alphaguide_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='landingg.alphaguide')),
            ],
            bases=('landingg.alphaguide',),
        ),
    ]
