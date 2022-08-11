# Generated by Django 4.1 on 2022-08-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'категорії', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='newsevents',
            options={'ordering': ['-created_at', 'id'], 'verbose_name': 'Новини', 'verbose_name_plural': 'Новини'},
        ),
        migrations.AlterField(
            model_name='newsevents',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Час публікації'),
        ),
        migrations.AlterField(
            model_name='newsevents',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]