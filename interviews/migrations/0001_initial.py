# Generated by Django 4.1 on 2022-09-04 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('interview_type', models.CharField(choices=[('phone', 'P'), ('tech', 'T'), ('code', 'C'), ('final', 'F')], max_length=100)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_applicant', to='users.applicant')),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_interviewer', to='users.interviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('interview', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='interview_feedback', to='interviews.interview')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_interview', to='interviews.interview')),
            ],
        ),
    ]
