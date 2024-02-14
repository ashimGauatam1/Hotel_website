from django.db import models

# Create your models here.

class Contact(models.Model):
    First=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)
    def __str__(self):
        return self.First
    
class bookr(models.Model):
    firstname=models.CharField(max_length=20)
    last=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    add=models.CharField(max_length=20)    
    city=models.CharField(max_length=20)
    room=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstname+self.last
    

class register_customer(models.Model):
    firstname=models.CharField(max_length=20)
    last=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    add=models.CharField(max_length=20)
  #  arrival_date = models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    room=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    enterby=models.CharField(max_length=20)