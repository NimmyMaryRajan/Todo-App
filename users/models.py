from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class userprofile(models.Model):
    def __str__(self):
        return str(self.username)
    userobj = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=700, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
