# Generated by Django 3.2.4 on 2021-06-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('fone', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
    ]
