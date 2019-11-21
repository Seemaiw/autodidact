import os
import uuid
from django.db import models

def get_image_path(_, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('posts', filename)

class Category(models.Model):
    name = models.CharField(max_length=20)

# Create your models here.
class Post(models.Model):
    topic = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
