# Generated by Django 5.0.1 on 2024-03-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_merge_0012_menuitem_available_0013_menuitem_allergy'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitercall',
            name='origin',
            field=models.CharField(choices=[('CUS', 'Customer'), ('KIT', 'Kitchen')], default='CUS', max_length=3),
        ),
    ]
