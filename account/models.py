from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import AbstractUser

class CostomUserManager(BaseUserManager):
    def create_user(self,email,password,**extrafields):
        email=self.normalize_email(email)

        user=self.model(
            email=email,
            **extrafields
        )
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,email,password,**extrafields):
        extrafields['is_staff']=True
       
        extrafields['is_superuser']=True


        if extrafields['is_staff'] is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extrafields['is_superuser'] is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email=email,password=password,**extrafields) 
        

class User(AbstractUser):
    email=models.CharField(max_length=80,unique=True)
    username=models.CharField(max_length=45)
    date_of_birth=models.DateField(null=True)

    object=CostomUserManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]
    #settings.py file AUTH_USER_MODEL

    def __str__(self):
        return self.username