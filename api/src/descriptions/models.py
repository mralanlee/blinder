from django.db import models
from users.models import User

# Create your models here.
class Description(models.Model):
    title = models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField(null=False, blank=False)
    emoji = models.CharField(max_length=150,null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)