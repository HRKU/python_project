# Generated by Django 4.1.6 on 2023-02-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_skill_is_code_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]