from django.db import models
from django.conf import settings
from django.utils.text import slugify
from froala_editor.fields import FroalaField


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=100, unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=35)
    url = models.SlugField(max_length=100, unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag'


class Post(models.Model):
    """
    Stores a single blog entry, related to :model:`auth.User`.
    """
    title = models.CharField(max_length=100)
    content = FroalaField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    abstract = FroalaField(max_length=200)
    cover_image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(
        Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    url = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
