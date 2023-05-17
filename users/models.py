from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher =models.BooleanField(default=False)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(default='.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'