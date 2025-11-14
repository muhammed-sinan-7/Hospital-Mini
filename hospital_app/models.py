from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department , on_delete=models.CASCADE)
    experience = models.IntegerField()
    image = models.ImageField(upload_to='doctors/')
    def __str__(self):
        return self.name
    