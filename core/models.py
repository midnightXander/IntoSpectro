from django.db import models
from datetime import datetime
class Profile(models.Model):
    sub_email = models.CharField(max_length=70)
    sub_topic = models.TextField()
    sub_start_date = models.DateTimeField()
    sub = models.BooleanField(default=False)
    sent_free_emails = models.IntegerField(default=0)
    sent_prem_emails = models.IntegerField(default=0)
    sub_end_date = models.DateTimeField(blank=True)