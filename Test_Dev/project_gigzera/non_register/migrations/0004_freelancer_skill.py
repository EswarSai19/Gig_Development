# Generated by Django 5.1.4 on 2025-01-17 03:34

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
import non_register.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_register', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('userId', models.CharField(default=non_register.models.generate_freelancer_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='freelancer/profile_pics/')),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_role', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('social_media', models.URLField(blank=True, null=True)),
                ('education', models.CharField(max_length=255)),
                ('certifications', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None)),
                ('experience', models.FloatField()),
                ('skills', models.JSONField(default=dict)),
                ('password', models.CharField(max_length=128)),
                ('projects_assigned', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None)),
                ('project_status', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('inprogress', 'In Progress'), ('completed', 'Completed'), ('not_started', 'Not Started')], max_length=50), blank=True, default=list, size=None)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('experience_years', models.PositiveIntegerField()),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='non_register.freelancer')),
            ],
        ),
    ]
