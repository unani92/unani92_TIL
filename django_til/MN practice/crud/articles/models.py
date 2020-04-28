from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 목적어가 되는 모델에 주로 정의를 함
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles',
    )