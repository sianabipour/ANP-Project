# Generated by Django 5.0.1 on 2024-01-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.CharField(choices=[('three', '3'), ('six', '6')], default='size', max_length=50, verbose_name='size'),
            preserve_default=False,
        ),
    ]
