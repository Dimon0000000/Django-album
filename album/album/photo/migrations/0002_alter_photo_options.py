# Generated by Django 5.0.3 on 2024-03-14 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-created_at']},
        ),
    ]
