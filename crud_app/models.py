from django.db import models

# Create your models here.
class tbl_Employee(models.Model):
    id=models.AutoField(primary_key=True,serialize=True)
    name=models.CharField(max_length=100,null=True, blank=True)
    email=models.CharField(max_length=100,null=True, blank=True)
    mobile_no = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        db_table="tbl_employee"
    
