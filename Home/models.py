from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    msg = models.TextField()
    dateTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"You've got a Message from {self.name} '{self.email}'"

