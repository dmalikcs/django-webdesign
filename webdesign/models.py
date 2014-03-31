from django.db import models
from django.forms import ModelForm

class SocialLinks(models.Model):
    facebook = models.CharField(
        max_length=30,
    )
    linkedin = models.CharField(
        max_length=40,
    )

    def __unicode__(self):
        return self.facebook


