from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone
from django.conf import settings

# Create your models here.
class todomodel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length = 500)
    startdate = models.DateField()
    enddate = models.DateField()
    