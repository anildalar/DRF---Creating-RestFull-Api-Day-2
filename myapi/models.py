from django.db import models

# Create your models here.

# OOps Inheritance

class Hero(models.Model):
    #1. Properties
    fullname = models.CharField(max_length=100) 
    alias = models.CharField(max_length=100)
    
    #2. Constructor
    
    #3. MEthod
    # Magic methods/Dunder Method   __anil__()
    def __str__(self): # self is a class internal object
        return self.fullname #object.property
       
    
    
    #4. Nested Class
    pass
