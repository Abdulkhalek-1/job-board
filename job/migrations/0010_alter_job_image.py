# Generated by Django 4.2.2 on 2023-06-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='jobs/%d-%m-%Y'),
        ),
    ]