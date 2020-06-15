from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='forum_user',
                                related_query_name='forum_user')

    picture = models.ImageField(default='avatar.jpg')  #default="discord.png"
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Threads(models.Model):
    author = models.ForeignKey(ForumUser, on_delete=models.CASCADE, related_name='threads',
                               related_query_name='threads')
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return str(self.author) + ' ' + self.title


class Posts(models.Model):
    author = models.ForeignKey(ForumUser, on_delete=models.CASCADE, related_name='posts',
                               related_query_name='posts')
    thread = models.ForeignKey(Threads, on_delete=models.CASCADE, related_name='posts',
                               related_query_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)

    content = models.TextField()

    def __str__(self):
        return str(self.author)


class Comments(models.Model):
    author = models.ForeignKey(ForumUser, on_delete=models.CASCADE, related_name='comments',
                               related_query_name='comments')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments',
                             related_query_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return str(self.author)
