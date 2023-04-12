from django.db import models
from froala_editor.fields import FroalaField


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    order = models.IntegerField()
    css_classes = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
        verbose_name = 'Menu Link'


class Menu(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(
        MenuItem, related_name='menu_items', related_query_name='item')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Menu'


class Header(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField()
    small_logo = models.ImageField(default=" ")
    featured_image = models.FileField(null=True, blank=True)
    featured_image_mobile = models.FileField(null=True, blank=True)
    menu = models.ForeignKey(Menu, blank=True, null=True,
                             related_name='menu_header', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Header"


class Footer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(blank=True, null=True)
    menu = models.ForeignKey(Menu, blank=True, null=True,
                             related_name='menu_footer', on_delete=models.PROTECT)
    bottom_text = FroalaField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Footer"


class MediaGallery(models.Model):

    VIDEO = 'VIDEO'
    AUDIO = 'AUDIO'

    PROVEEDOR_CHOICES = (
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
    )
    type = models.CharField(
        choices=PROVEEDOR_CHOICES,
        default=VIDEO,
    )
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    key = models.CharField(max_length=50)
    html_wrapper = models.CharField(
        max_length=1000, default='<iframe></iframe>')

    def __str__(self):
        return self.name

    def is_upperclass(self):
        return self.type in (self.VIDEO, self.AUDIO)
    
    class Meta:
        verbose_name_plural = 'Media Galleries'


class Slider(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField()
    link = models.URLField(null=True, blank=True, max_length=200)
    show_text = models.BooleanField(default=True)
    order = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        ordering = ('order',)