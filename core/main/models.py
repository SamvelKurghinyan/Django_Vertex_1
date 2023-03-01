from django.db import models

# Create your models here.
class HomeBG(models.Model):
    img = models.ImageField('Home BG', upload_to='media')


class Post(models.Model):
    name = models.CharField('Post name', max_length=50)
    text = models.TextField('Post text')
    img = models.ImageField('Post image', upload_to='media')
    date = models.DateTimeField('Post date')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
