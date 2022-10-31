from unicodedata import category
from django.db import models
from django.urls import reverse


class Notes(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #reverse homepage
        return reverse('Notes:home')