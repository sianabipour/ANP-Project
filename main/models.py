from django.db import models
from django.utils.translation import gettext_lazy as _

class Slide(models.Model):
    
    image_fa = models.ImageField(_("image_fa"), upload_to='Slide')
    image_en = models.ImageField(_("image_en"), upload_to='Slide')
    
    link = models.URLField(_("link"), max_length=50 , blank=True , null=True)
    
    def __str__(self):
        return f'{self.pk}'   
    
class Customer(models.Model):
    
    image = models.ImageField(_("image"), upload_to='Customer')
