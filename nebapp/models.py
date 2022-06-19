from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Neighborhood(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    population = models.IntegerField(default=0)
    
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=200,blank=True,null=True)
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='pics/',blank=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    # is_admin = models.BooleanField(default=False)

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()
    
    # def __str__(self):
    #     return self.name

class Business(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='pics/',blank=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='pics/',blank=True,null=True)
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    def __str__(self):
        return self.title