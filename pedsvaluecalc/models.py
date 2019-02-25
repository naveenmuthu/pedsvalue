from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.TextField(max_length=75, blank=False)

class test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,unique=True,max_length=240)
    # TODO: ALlow null here
    abbrev = models.CharField(max_length=10)
    # TODO: ALlow null here
    synonym = models.CharField(max_length=240)
    cost = models.IntegerField(null=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()
