from django.db import models
from django.utils.text import slugify

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)
    url = models.SlugField(max_length=100, unique=True, editable=False)
	
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Products Categories'

class Product(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=300)
    sku = models.CharField(max_length=50)
    iframe_soundcloud_large = models.CharField(blank=True, null=True, max_length=1000,default='<iframe></iframe>')
    iframe_soundcloud_small = models.CharField(blank=True, null=True, max_length=1000,default='<iframe></iframe>')
    price = models.CharField(blank=True, null=True, max_length=20)
    image = models.FileField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, related_name='product_category', on_delete=models.PROTECT)
    file = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=100, unique=True, editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"

