# Generated by Django 5.1.1 on 2024-09-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0002_remove_salearticles_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='salearticles',
            name='categorie',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
    ]
