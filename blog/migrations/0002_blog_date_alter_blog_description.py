# Generated by Django 5.0.1 on 2024-01-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=70),
        ),
    ]
