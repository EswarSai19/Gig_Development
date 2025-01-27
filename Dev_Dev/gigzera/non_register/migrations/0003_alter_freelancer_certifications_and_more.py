# Generated by Django 5.1.5 on 2025-01-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_register', '0002_alter_freelancer_phone_alter_freelancer_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='certifications',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='project_status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='projects_assigned',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
