from django.db import models
from django.contrib.auth.models import  User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    style =models.CharField(max_length=50, null=True)


    def __str__(self):
        return 'user {}'.format(self.user.username)

'''
class user_img(models.Model):
    img_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=50)
    headimg = models.FileField(upload_to='user_imgs',default='')
'''

#存储模板时用上
class img(models.Model):
    name = models.CharField(max_length=50)
    headimg = models.FileField(upload_to="xiaoxin/",default=" ")

    def __str__(self):
        return self.name
