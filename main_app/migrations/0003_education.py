# Generated by Django 5.0.6 on 2024-09-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('collagename', models.CharField(max_length=300)),
                ('skill', models.CharField(blank=True, max_length=300, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
    ]
