# Generated by Django 4.0.1 on 2022-11-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainhomeapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('phone', models.TextField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'user_signup',
            },
        ),
    ]