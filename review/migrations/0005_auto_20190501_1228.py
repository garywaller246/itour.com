# Generated by Django 2.2 on 2019-05-01 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_tour', to='tour.Tour'),
        ),
    ]
