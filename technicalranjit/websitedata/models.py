
from django.db import models
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User





class ForumPost(models.Model):
    title=models.CharField(max_length=100,default="",blank=True)
    images=models.ImageField(upload_to='ForumImage',null=True,blank=True)
    description=models.TextField(max_length=250,blank=True)
    user=models.ForeignKey(User,on_delete='CASCADE')
    upload_date=models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete='Cascade')
    description=models.CharField(max_length=100,blank=True,default="Add Description")
    city=models.CharField(max_length=20,blank=True,default="Add your City")
    Website=models.CharField(max_length=20,blank=True,default="Add your Website")
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True,default="/profile_pic/default.png")
    cover_pic=models.ImageField(upload_to='cover_pic',blank=True,default="profile_pic.jpg")

    london = UserProfileManager()


    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)



