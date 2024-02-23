from django.db import models

# blurts are short form textual media content, limited to 280 characters.
# Post => user (posting the content), no. of chars, date published, edited?


class Post(models.Model):
    content = models.CharField(max_length=280)
    pub_date = models.DateTimeField("date published")
