from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    used_time = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)++ ": Rs" + str(self.price)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
