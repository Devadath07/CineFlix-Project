from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

#creating custom user model

#abstractuser is used to get all data in the user model (default django model)

class RoleChoices(models.TextChoices):

    USER = 'User','User'

    ADMIN = 'Admin','Admin'



class Profile(AbstractUser):

    role = models.CharField(max_length=10,choices=RoleChoices.choices)

    phone = models.CharField(null=True,blank=True) # next is signup view in post method we doing post method to add this to model while adding there in ph no in signup model

    class Meta :

        verbose_name = 'Profile'

        verbose_name_plural = 'Profile'

    def __str__(self):
            
        return f'{self.username}'
    

