from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    suite = models.CharField(max_length=30, blank=False, null=False)
    city = models.CharField(max_length=30, blank=False, null=False)
    zipcode = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def qtd_posts(self):
        return self.posts.all().count()

    @property
    def qtd_comments_by_post(self):
            return Comment.objects.filter(post_id__user_id=self).all().count()

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    body = models.CharField(max_length=500, blank=False, null=False)
    user_id = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    @property
    def qtd_comments(self):
        return self.comments.all().count()

class Comment(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50)
    body = models.CharField(max_length=500, blank=False, null=False)
    post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


