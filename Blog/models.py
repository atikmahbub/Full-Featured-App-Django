from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 200)
    date_posted = models.DateTimeField(default = timezone.now)
    authors = models.ForeignKey( User, on_delete= models.CASCADE , blank = True , null = True)

    def get_absolute_url(self):
        return reverse('blog-detail' , kwargs= {'pk' : self.pk })