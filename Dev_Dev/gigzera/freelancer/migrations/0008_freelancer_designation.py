# Generated by Django 5.1.5 on 2025-02-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0007_alter_projectquote_freelancer'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='designation',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
