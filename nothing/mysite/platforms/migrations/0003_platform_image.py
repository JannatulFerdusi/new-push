# Generated by Django 5.0.4 on 2024-04-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0002_remove_platform_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
