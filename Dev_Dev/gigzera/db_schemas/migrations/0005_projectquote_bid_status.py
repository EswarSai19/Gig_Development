# Generated by Django 5.1.5 on 2025-02-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_schemas', '0004_alter_projectquote_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectquote',
            name='bid_status',
            field=models.CharField(default='Not confrimed yet', max_length=20),
        ),
    ]
