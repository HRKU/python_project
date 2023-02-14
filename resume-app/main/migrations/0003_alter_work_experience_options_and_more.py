# Generated by Django 4.1.6 on 2023-02-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_work_experience_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work_experience',
            options={'ordering': ['Title'], 'verbose_name': 'Work_Experience', 'verbose_name_plural': 'Work_Experiences'},
        ),
        migrations.AddField(
            model_name='work_experience',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='work_experience',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]