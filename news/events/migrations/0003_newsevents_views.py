# Generated by Django 4.1 on 2022-08-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_category_options_alter_newsevents_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsevents',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
