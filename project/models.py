from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.urls import reverse


class Project(models.Model):
    slug = models.SlugField(_("slug"), unique=True)
    
    name_fa = models.CharField(_("name_fa"), max_length=150)
    name_en = models.CharField(_("name_en"), max_length=150)
    
    content_fa = HTMLField(_("content_fa"))
    content_en = HTMLField(_("content_en"))
    
    image_fa = models.ImageField(_("image_fa"), upload_to='Project')
    image_en = models.ImageField(_("image_en"), upload_to='Project')

    meta_description_fa = models.TextField(_("meta_description_fa"))
    meta_description_en = models.TextField(_("meta_description_en"))
    
    icon = models.CharField(_("icon"), max_length=20,help_text="Fontawesome Class Name")
    
    size_choices = (
        ('3', 'three'),
        ('6', 'six'),
    )
    order_number = models.IntegerField(_("order_number"),default=0)
    size = models.CharField(_("size"),choices=size_choices, max_length=50)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return f'{self.name_fa} - {self.name_en}'

    def get_absolute_url(self):
        return reverse("project", kwargs={"slug": self.slug})


