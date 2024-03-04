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
        return reverse("shop_category", kwargs={"slug": self.slug})


class Product(models.Model):
    slug = models.SlugField(_("slug"))
    
    title_fa = models.CharField(_("title_fa"), max_length=150)
    title_en = models.CharField(_("title_en"), max_length=150)
    
    content_fa = HTMLField(_("content_fa"))
    content_en = HTMLField(_("content_en"))
    
    image_fa = models.ImageField(_("image_fa"), upload_to='Product')
    image_en = models.ImageField(_("image_en"), upload_to='Product')
    
    date_update = models.DateField(_("date_update"), auto_now=True)
    date_create = models.DateField(_("date_create"), auto_now_add=True)
    
    tags = models.ManyToManyField("shop.Tag", verbose_name=_("tags"))
    icon = models.CharField(_("icon"), max_length=20,help_text="Fontawesome Class Name")
    
    price = models.IntegerField(_("price"))
    
    category = models.ForeignKey("shop.Category", verbose_name=_("category"), on_delete=models.CASCADE,related_name='products')

    meta_description_fa = models.TextField(_("meta_description_fa"))
    meta_description_en = models.TextField(_("meta_description_en"))
    
    creator = models.ForeignKey("account.Profile", verbose_name=_("creator"), on_delete=models.CASCADE)
    
    views = models.IntegerField(_("views"), default=0)
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f'{self.title_fa} - {self.title_en}'

    def get_absolute_url(self):
        return reverse("Product", kwargs={"slug": self.slug})


class Tag(models.Model):
    name_fa = models.CharField(_("name_fa"), max_length=150)
    name_en = models.CharField(_("name_en"), max_length=150)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return f'{self.name_fa} - {self.name_en}'

class Comment(models.Model):

    user = models.CharField(_("user"), max_length=150)    
    email = models.EmailField(_("email"), max_length=254)

    date_create = models.DateField(_("date_create"), auto_now_add=True)
    
    comment_description = models.TextField(_("comment_description"))
    
    product_table = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="comments",null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'
    