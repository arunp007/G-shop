# Generated by Django 4.0.1 on 2022-11-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('price', models.TextField(max_length=50)),
                ('image', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
    ]
