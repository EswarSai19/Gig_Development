# Generated by Django 5.1.5 on 2025-02-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_schemas', '0005_projectquote_bid_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectquote',
            name='admin_margin',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
