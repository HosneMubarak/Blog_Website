from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from users.models import CustomUser


class NewsCategory(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name


class NewsModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField()
    image1 = models.ImageField(upload_to='news_photo/%Y/%m/%d/', blank=True, null=True)
    image2 = models.ImageField(upload_to='news_photo/%Y/%m/%d/', blank=True, null=True)
    published_date = models.DateField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(NewsModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list-detail', kwargs={'slug': self.slug})


class CommentModel(models.Model):
    article = models.ForeignKey(NewsModel, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse('list-detail', kwargs={'slug': self.slug})
