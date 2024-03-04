from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class Category(models.Model):
    slug = models.SlugField(_("slug"), unique=True)
    
    name_fa = models.CharField(_("name_fa"), max_length=150)
    name_en = models.CharField(_("name_en"), max_length=150)
    
    content_en = HTMLField(_("content_en"))
    content_fa = HTMLField(_("content_fa"))
    
    image_en = models.ImageField(_("image_en"), upload_to='Category')
    image_fa = models.ImageField(_("image_fa"), upload_to='Category')

    meta_description_fa = models.TextField(_("meta_description_fa"))
    meta_description_en = models.TextField(_("meta_description_en"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return f'{self.name_fa} - {self.name_en}'

    def get_absolute_url(self):
        return reverse("service_category", kwargs={"slug": self.slug})


class Service(models.Model):
    slug = models.SlugField(_("slug"))
    
    title_fa = models.CharField(_("title_fa"), max_length=150)
    title_en = models.CharField(_("title_en"), max_length=150)
    
    content_en = HTMLField(_("content_en"))
    content_fa = HTMLField(_("content_fa"))
    
    image_en = models.ImageField(_("image_en"), upload_to='Service')
    image_fa = models.ImageField(_("image_fa"), upload_to='Service')
    
    date_update = models.DateField(_("date_update"), auto_now=True)
    date_create = models.DateField(_("date_create"), auto_now_add=True)
    
    tags = models.ManyToManyField("service.Tag", verbose_name=_("tags"))
    icon = models.CharField(_("icon"), max_length=20,help_text="Fontawesome Class Name")
        
    meta_description_fa = models.TextField(_("meta_description_fa"))
    meta_description_en = models.TextField(_("meta_description_en"))
    
    attached_file = models.FileField(_("attached_file"), upload_to='Service',null=True,blank=True)
    
    creator = models.ForeignKey("account.Profile", verbose_name=_("creator"), on_delete=models.CASCADE,related_name="services")
    
    views = models.IntegerField(_("views"), default=0)
    
    category = models.ForeignKey("service.Category", verbose_name=_("category"), on_delete=models.CASCADE,related_name="services")
    
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return f'{self.title_fa} - {self.title_en}'

    def get_absolute_url(self):
        return reverse("service", kwargs={"slug": self.slug})


class Tag(models.Model):
    name_fa = models.CharField(_("name_fa"), max_length=150)
    name_en = models.CharField(_("name_en"), max_length=150)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return f'{self.name_fa} - {self.name_en}'

class RequestedService(models.Model):
    
    phone = models.CharField(_("phone"), max_length=12)
    service = models.ForeignKey("service.Service", verbose_name=_("service"), on_delete=models.CASCADE,related_name="requested_services")
    def __str__(self):
        return f'{self.phone} - {self.service.title_fa}'
    
    
    