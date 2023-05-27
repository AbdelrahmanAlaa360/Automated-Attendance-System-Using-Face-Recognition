from django.db import models
from django.contrib.auth.models import AbstractUser
import os

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher =models.BooleanField(default=False)


def profile_image_upload_to(instance, filename):
    username = instance.user.username
    upload_path = os.path.join('profile_pics', username, filename)
    return upload_path

class ProfileImage(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(default='.jpg', upload_to=profile_image_upload_to,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class TrainImage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='trainImage')
    image = models.ImageField(default='.jpg', upload_to=profile_image_upload_to)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
