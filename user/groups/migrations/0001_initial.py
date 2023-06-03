# Generated by Django 4.2.1 on 2023-06-03 00:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id_group', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
