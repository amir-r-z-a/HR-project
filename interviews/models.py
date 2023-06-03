from django.db import models
from users.models import *
#from ..users.models import *


class Interview(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()
    interview_types = [
        ('phone', 'P'),
        ('tech', 'T'),
        ('code', 'C'),
        ('final', 'F'),
    ]
    interview_type = models.CharField(max_length=100, choices=interview_types)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE,
                                    related_name='interview_interviewer')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='interview_applicant')


class Comment(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='comment_interview')
    comment_text = models.TextField()


class Feedback(models.Model):
    feedback_text = models.TextField()
    interview = models.OneToOneField(Interview, on_delete=models.CASCADE, related_name='interview_feedback')
