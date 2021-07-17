from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)
    bio = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=30, blank=True)
    relationship = models.CharField(max_length=255,blank=True)
    age = models.CharField(max_length=2, blank=True,null=True)
    birth_date = models.DateField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=12,blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
    
    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Follow(models.Model):
    user = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User,related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)