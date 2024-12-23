from django.db import models
from uuid import uuid4


# Create your models here.
class Post(models.Model):
    id = models.CharField(
        max_length=100, unique=True, default=uuid4, primary_key=True, editable=False
    )
    title = models.CharField(max_length=500)
    image = models.URLField()
    body = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)

    # change title of posts to post title
    def __str__(self):
        return str(self.title)

    class Meta:
        # order by latest post added to DB
        ordering = ["-created_date"]
