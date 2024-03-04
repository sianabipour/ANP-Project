# Generated by Django 5.0.1 on 2024-01-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0004_remove_faq_shomare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question',
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(default='test', verbose_name='answer_en'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_fa',
            field=models.TextField(default='test', verbose_name='answer_fa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.CharField(default='test', max_length=50, verbose_name='question_en'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='question_fa',
            field=models.CharField(default='test', max_length=50, verbose_name='question_fa'),
            preserve_default=False,
        ),
    ]
