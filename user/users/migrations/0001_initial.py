# Generated by Django 4.2.1 on 2023-06-02 23:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
            ],
        ),
    ]
