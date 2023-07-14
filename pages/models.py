from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class ChatMessage(models.Model):
	#user = models.TextField(null=False)
	message = models.TextField()
	reply = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)