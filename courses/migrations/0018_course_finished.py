# Generated by Django 4.2.14 on 2024-10-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_alter_projectsubmission_learning_in_public_links_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='finished',
            field=models.BooleanField(default=False, help_text='Whether the course has finished.'),
        ),
    ]
