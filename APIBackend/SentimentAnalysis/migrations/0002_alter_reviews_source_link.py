# Generated by Django 4.1.13 on 2024-08-25 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SentimentAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='source_link',
            field=models.TextField(max_length=100, null=True),
        ),
    ]