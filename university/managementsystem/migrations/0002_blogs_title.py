# Generated by Django 3.2.7 on 2021-09-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='title',
            field=models.CharField(default='', max_length=32),
        ),
    ]
