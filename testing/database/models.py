from django.db import models

# Create your models here.
class College(models.Model):
    college_code=models.AutoField(primary_key=True)
    
