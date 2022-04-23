from django.db import models

# Create your models here.


class Post(models.Model):
    Topic = models.CharField(max_length=250, default='')
    Desc = models.CharField(max_length=750, default='')
    Preview_img = models.ImageField(blank=True)
    # image = models.FileField(blank=True)

    def __str__(self):
        return str(self.Topic)


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return str(self.post)
