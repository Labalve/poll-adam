# Generated by Django 2.1.4 on 2019-02-06 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_question_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='audio'),
        ),
    ]