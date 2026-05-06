from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid
# Create your models here.

class ControlUsers(AbstractUser):
    phon=models.CharField(max_length=25,default=123456789,blank=False,null=False)
    imgs=models.ImageField(upload_to='images/',default='images/default.jpg',blank=True,null=False)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=False)
    slug = models.SlugField(blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            uid = str(uuid.uuid4())[:5]
            self.slug = slugify(f"{self.username}-{uid}")

        super().save(*args, **kwargs)

