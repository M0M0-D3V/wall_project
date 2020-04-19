from django.db import models
from login_app.models import Users
# Create your models here.


class Messages(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(
        Users, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Message ID:({self.id}): {self.message} - {self.user}"


class Comments(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(
        Users, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(
        Messages, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Comment ID:({self.id}): {self.comment} on {self.message} by {self.user}"
