# Generated by Django 4.1.7 on 2024-01-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='on_hold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.DecimalField(decimal_places=1, help_text='inches', max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='$ (CAD)', max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.DecimalField(decimal_places=1, help_text='inches', max_digits=10),
        ),
    ]
