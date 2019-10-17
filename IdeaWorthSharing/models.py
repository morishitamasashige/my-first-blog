from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

class IdeaTweet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    context = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
