from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Story(models.Model):
    created_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    text = RichTextField()
    # text = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('story-list')
        # return reverse('story-detail', kwargs={'pk': self.pk})
    