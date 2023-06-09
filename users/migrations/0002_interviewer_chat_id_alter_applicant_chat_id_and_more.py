# Generated by Django 4.1 on 2022-09-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewer',
            name='chat_id',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='chat_id',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='telegram_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
