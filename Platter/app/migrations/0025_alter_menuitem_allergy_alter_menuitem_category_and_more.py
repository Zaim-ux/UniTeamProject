# Generated by Django 5.0.1 on 2024-03-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_merge_20240319_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='allergy',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('mains', 'Main'), ('drinks', 'Drink'), ('desserts', 'Dessert'), ('starters', 'Starter')], default='mains', max_length=30),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(default='Delicious meal', max_length=120),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menuItemID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='spice',
            field=models.CharField(choices=[('spiceless', 'Spiceless'), ('hot', 'Hot'), ('atomic', 'Atomic'), ('mild', 'Mild')], default='spiceless', max_length=15),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('RTC', 'Ready to collect'), ('COM', 'Completed'), ('REC', 'Received'), ('UPD', 'Not paid for'), ('CKG', 'Cooking')], max_length=3),
        ),
        migrations.AlterField(
            model_name='waitercall',
            name='message',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='waitercall',
            name='waiterCallID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
