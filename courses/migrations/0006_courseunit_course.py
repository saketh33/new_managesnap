# Generated by Django 4.0 on 2021-12-19 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_mycourseunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseunit',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
