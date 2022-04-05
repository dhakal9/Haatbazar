from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    photo = models.ImageField(default='default.jpg', upload_to='post_pic')
    def __str__(self):
        return str(self.photo)+ ": Rs" + str(self.price)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
