from django.db import models
from userplate.models import User

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    score = models.IntegerField()
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

