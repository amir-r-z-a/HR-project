from datetime import date, timedelta
from rest_framework import serializers
from .models import *
#from ..users.models import *
#from ..users.serializer import *

from users.models import *
from users.serializer import *

import datetime

class InterviewSerializer(serializers.ModelSerializer):
    interviewer_id = serializers.IntegerField(write_only=True)
    applicant_id = serializers.IntegerField(write_only=True)
    date = serializers.DateTimeField()
    interviewer = InterviewerSerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True)
    def save(self, **kwargs):
        applicant_id = self.validated_data.pop('applicant_id')
        applicant: Applicant = Applicant.objects.filter(pk=applicant_id)[0]
        interviewer_id = self.validated_data.pop('interviewer_id')
        interviewer: Interviewer = Interviewer.objects.filter(pk=interviewer_id)[0]
        #date = self.validated_data.pop('date')-timedelta(hours=4,minutes=30)
        interview: Interview = super().save(applicant=applicant, interviewer=interviewer, **kwargs)
        return interview

    class Meta:
        model = Interview
        fields = (
            'interviewer_id',
            'applicant_id',
            'interview_type',
            'interviewer',
            'applicant',
            'date'
        )


