# Generated by Django 5.1.5 on 2025-02-01 21:00

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_faq_answer_bn_faq_answer_hi'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_bn',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Answer (Bengali)'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_hi',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Answer (Hindi)'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, verbose_name='Question (Bengali)'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(blank=True, verbose_name='Question (Hindi)'),
        ),
    ]
