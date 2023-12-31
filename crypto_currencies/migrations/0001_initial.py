# Generated by Django 4.2.3 on 2023-07-17 21:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.CharField(max_length=15)),
                ('total_supply', models.BigIntegerField(null=True)),
                ('price', models.PositiveBigIntegerField(null=True)),
                ('market_cap', models.PositiveBigIntegerField(null=True)),
                ('volume_change_24h', models.FloatField(null=True)),
                ('percent_change_24h', models.FloatField(null=True)),
                ('user_favourite', models.ManyToManyField(related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name', 'price'],
                'indexes': [models.Index(fields=['name', 'slug'], name='crypto_curr_name_b3a6f4_idx')],
            },
        ),
    ]
