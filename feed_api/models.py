from django.db import models
from django.conf import settings
# Create your models here.
class ProfileFeedItem(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status=models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status