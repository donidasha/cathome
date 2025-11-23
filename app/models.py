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
    
class Volunteer(models.Model):
        name = models.CharField(max_length=150)
        phone_number = models.CharField(max_length=150)
        email = models.EmailField()
        
        def __str__(self):
                return self.name
        
class Application(models.Model):
        name = models.CharField(max_length=150)
        email = models.EmailField()
        phone_number = models.CharField(max_length=150)
        comment = models.TextField()
        cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.name
        

    
