# Generated by Django 4.0 on 2024-01-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='questoin')),
                ('answer', models.TextField(verbose_name='answer')),
            ],
        ),
    ]