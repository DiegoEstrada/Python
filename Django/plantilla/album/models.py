from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
#from django.conf import settings

# Create your models here.

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(User , on_delete=models.PROTECT,null=True)
    title = models.CharField(max_length=50, default="No tittle")
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now=True)
    favorite = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo-list')

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    instance.photo.delete(True)

