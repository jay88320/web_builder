# Generated by Django 3.1.1 on 2021-03-08 02:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_element_table', models.CharField(max_length=200)),
                ('page_element_table_id', models.IntegerField()),
                ('page_element_order', models.IntegerField()),
                ('page_element_is_active', models.BooleanField(default=1)),
                ('page_element_file', models.CharField(max_length=200)),
                ('page_element_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_element_updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_element_page_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.page')),
            ],
        ),
    ]
