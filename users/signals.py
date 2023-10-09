from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import userprofile


# @receiver(post_save, sender=Profile)


def createUser(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = userprofile.objects.create(
            userobj=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.userobj

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.userobj
        user.delete()
    except:
        pass


post_save.connect(createUser, sender=User)
post_save.connect(updateUser, sender=userprofile)
post_delete.connect(deleteUser, sender=userprofile)
