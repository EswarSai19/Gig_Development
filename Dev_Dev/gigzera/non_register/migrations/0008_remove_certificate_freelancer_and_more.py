# Generated by Django 5.1.5 on 2025-02-01 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('non_register', '0007_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='freelancer',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='freelancer',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='freelancer',
        ),
        migrations.DeleteModel(
            name='ProjectsDisplay',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='EmploymentHistory',
        ),
        migrations.DeleteModel(
            name='Freelancer',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
