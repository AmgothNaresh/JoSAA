# Generated by Django 4.2.2 on 2024-06-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=255)),
                ('Branch', models.CharField(max_length=255)),
                ('Category', models.CharField(default='OPEN', max_length=255)),
                ('Gender', models.CharField(default='Gender-Neutral', max_length=255)),
                ('Opening_rank', models.FloatField(default=1)),
                ('Closing_rank', models.FloatField(default=99999)),
                ('year', models.FloatField(default=2020)),
                ('round', models.IntegerField(default=1)),
            ],
        ),
    ]
