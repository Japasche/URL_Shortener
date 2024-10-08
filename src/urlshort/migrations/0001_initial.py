# Generated by Django 5.1.1 on 2024-09-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=700)),
                ('short_url', models.CharField(max_length=100)),
                ('time_date_created', models.DateTimeField()),
            ],
        ),
    ]
