# Generated by Django 5.1.5 on 2025-02-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_schemas', '0009_projectquote_revised_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectquote',
            name='currency',
            field=models.CharField(default='INR', max_length=10),
        ),
    ]
