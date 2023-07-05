# Generated by Django 4.1.1 on 2023-06-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_pages', '0006_category_alter_sound_author_alter_sound_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='file',
            field=models.FileField(null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]