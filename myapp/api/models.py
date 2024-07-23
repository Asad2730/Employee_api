from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='employee')
    
    def __str__(self) -> str:
        return self.name