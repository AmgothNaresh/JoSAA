# Generated by Django 4.2.2 on 2024-06-12 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_rename_data_josaa_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='josaa_data',
            old_name='institute',
            new_name='institue',
        ),
    ]