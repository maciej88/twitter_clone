from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)