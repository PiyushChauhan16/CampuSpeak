from django.db import models
import uuid

# Create your models here.
class user (models.Model):
    rollNo = models.CharField (max_length = 100)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    authPin = models.CharField (max_length=50)
    batch = models.CharField (max_length=50)
    branch = models.CharField (max_length=50)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.rollNo

    
class post (models.Model):
    uid = models.ForeignKey (user, on_delete=models.CASCADE, to_field = "uid")
    pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postContent = models.TextField()
    image = models.CharField (max_length = 100)

    def __str__(self):
        return str(self.uid)
    

class comment (models.Model):
    uid = models.ForeignKey (user, max_length=100, on_delete=models.CASCADE, to_field="uid")
    pid = models.ForeignKey (post, max_length = 100, on_delete=models.CASCADE, to_field = "pid")
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    replyId = models.CharField(max_length=100)
    commentContent = models.TextField()


class saved (models.Model):
    uid = models.ForeignKey (user, max_length=100, on_delete=models.CASCADE, to_field="uid")
    pid = models.ForeignKey (post, max_length = 100, on_delete=models.CASCADE, to_field = "pid")
   
class userSetting (models.Model):
    uid = uid = models.ForeignKey (user, max_length=100, on_delete=models.CASCADE, to_field="uid")
    isEnable = models.TextField (max_length=1, default = "1")

    def __str__ (self):
        return str(self.uid)