# Generated by Django 4.1.13 on 2024-08-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_1', models.IntegerField()),
                ('num_2', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=100)),
                ('source_link', models.CharField(max_length=100, null=True)),
                ('title', models.TextField(null=True)),
                ('description', models.TextField()),
                ('sentiment', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]