from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Snippet(models.Model):
    user=models.ForeignKey(User,default=1, null=True, on_delete=models.SET_NULL)
    blogname = models.CharField(max_length=100)
    blogauth = models.CharField(max_length=100)

    blogdes=models.TextField(max_length=400)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.blogname