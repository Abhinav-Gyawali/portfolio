from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class ChatMessage(models.Model):
	#user = models.TextField(null=False)
	message = models.TextField()
	reply = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	
	
class ListeningResource(models.Model):
    title = models.CharField(max_length=255)
    product_image = models.TextField()
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    url = models.TextField()
    desc = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)