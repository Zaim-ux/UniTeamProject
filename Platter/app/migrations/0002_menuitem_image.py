# Generated by Django 5.0.1 on 2024-01-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='MenuItemImages/default.png', upload_to='MenuItemImages/<django.db.models.fields.IntegerField>'),
            preserve_default=False,
        ),
    ]
