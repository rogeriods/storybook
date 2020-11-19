from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Story(models.Model):
    created_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # text = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('story-list')
        # return reverse('story-detail', kwargs={'pk': self.pk})
    