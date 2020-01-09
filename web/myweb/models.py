from django.db import models, connection

# Create your models here.

class UserManager(models.Manager):
    def getuserid(self):        
        return super().get_queryset().all

class UserInfo(models.Model):
    
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    
    objects = models.Manager()
    my_objects = UserManager()
    
    def __unicode__(self):
        return self.user
    

