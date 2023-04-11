from django.db import models
from django.conf import settings
from django.utils import timezone
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor

class Post(models.Model):
    """
    Stores a single blog entry, related to :model:`blog.Blog` and
    :model:`auth.User`.
    """
    title = models.CharField(max_length=100)
    content = FroalaField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    abstract = FroalaField(max_length=200)
    cover_img = models.ImageField(null=True, blank=True)
    #categoria = models.ForeignKey(Categoria, null=True, blank=True, related_name='items', on_delete=models.PROTECT)
    #tag = models.ManyToManyField(Tag, null=True, blank=True, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    slug = models.CharField(max_length=100)
	
    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    class Meta:
        verbose_name='Post'