# Generated by Django 3.1.1 on 2021-03-25 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_header_header_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='header_file',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
