# Generated by Django 2.2 on 2019-05-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20190502_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]