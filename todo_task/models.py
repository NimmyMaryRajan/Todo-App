from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import userprofile
import uuid
# Create your models here.

class task(models.Model):
    user = models.ForeignKey(userprofile, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=200)
    priority = models.DecimalField(max_digits=1,decimal_places=0,null=True,blank=True)
    star = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.task_name
    class Meta:
        ordering = ['priority']
