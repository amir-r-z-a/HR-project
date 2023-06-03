from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    resume = models.TextField()
    linkedin_address = models.URLField()
    age = models.PositiveIntegerField(default=0)
    chat_id = models.IntegerField(editable=False,null=True)
    sex_choices = (
        ('male', 'M'),
        ('female', 'F'),
    )
    sex = models.CharField(max_length=100, choices=sex_choices,default='M')
    status_choices = (
        ('pending', 'P'),
        ('confirmed', 'C'),
        ('failed', 'F'),
    )
    status = models.CharField(max_length=100, choices=status_choices,default='P')


class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Interviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=100,unique=True)
    chat_id = models.CharField(editable=False,max_length=100,null=True)

