# Generated by Django 4.2.15 on 2024-09-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]