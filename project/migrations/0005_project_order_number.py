# Generated by Django 5.0.1 on 2024-01-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order_number',
            field=models.IntegerField(default=0, verbose_name='order_number'),
        ),
    ]
