from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField()
    """URL to redirect to"""

    alias=models.CharField()
    """Alias to use after go/"""

    