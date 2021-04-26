from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    img_post = models.ImageField(upload_to="post_image/")
    caption = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.caption[:100]

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "USERNAME:" + str(self.user)
