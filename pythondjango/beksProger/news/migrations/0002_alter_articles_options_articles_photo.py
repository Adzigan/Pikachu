# Generated by Django 4.2.5 on 2023-10-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='articles',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]