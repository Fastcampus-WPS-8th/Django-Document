from django.db import models

__all__ = (
    'User',
    'PostBase',
    'PhotoPost',
    'TextPost',
)


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    photo_url = models.CharField(max_length=500)


class TextPost(PostBase):
    text = models.TextField()
