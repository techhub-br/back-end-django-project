# Generated by Django 5.0.7 on 2024-07-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('legend', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=25000)),
            ],
        ),
    ]
