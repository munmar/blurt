from django.db import models
from users.models import User


# blurts are short form textual media content, limited to 280 characters.
# Post => user (posting the content), no. of chars, date published, edited?
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.content