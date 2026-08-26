from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Published', 'Published'),
        ('REJECTED', 'Rejected'),
    ]
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=10)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


