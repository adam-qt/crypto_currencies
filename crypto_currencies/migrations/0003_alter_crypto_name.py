# Generated by Django 4.2.3 on 2023-07-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_currencies', '0002_rename_crypto_curr_name_b3a6f4_idx_crypto_curr_name_e798d6_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
