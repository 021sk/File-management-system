from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from file.models import Folder


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Folder.objects.create(owner=kwargs['instance'], name='root')

