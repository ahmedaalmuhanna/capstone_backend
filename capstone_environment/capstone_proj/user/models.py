from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField( null =True, blank = True) #update_to="media/",
    bio = models.TextField(blank=True)
    is_gov = models.BooleanField(default=False)
    def __str__(self) :
        return f"{self.user.username}"