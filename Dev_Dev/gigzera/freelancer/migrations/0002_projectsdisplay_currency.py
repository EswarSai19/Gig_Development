# Generated by Django 5.1.5 on 2025-02-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsdisplay',
            name='currency',
            field=models.CharField(default='INR', max_length=10),
        ),
    ]
