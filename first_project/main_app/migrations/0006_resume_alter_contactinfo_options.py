# Generated by Django 5.0.6 on 2024-11-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('resume_file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Resume',
            },
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name_plural': 'ContactInfos'},
        ),
    ]
