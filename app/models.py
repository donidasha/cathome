from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=150)
    discription = models.TextField()
    image = models.ImageField(upload_to='images/', 
            blank=True, null=True, default='images/default.jpg')
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', 
            blank=True, null=True, default='images/default2.jpg')
    def __str__(self):
        return self.name
    
    
