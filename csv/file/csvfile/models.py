from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150, blank=False, unique=True)
    profile = models.TextField()

    # representation of data in CLI or log
    def __str__(self):
        return self.name
