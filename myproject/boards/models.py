from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name        = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject      = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)
    board        = models.ForeignKey(Board, related_name='topics', on_delete=models.PROTECT)
    starter      = models.ForeignKey(User, related_name='topics', on_delete=models.PROTECT)

class Post(models.Model):
    message    = models.TextField(max_length=800)
    topic      = models.ForeignKey(Topic, related_name='posts', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    updateb_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.PROTECT)