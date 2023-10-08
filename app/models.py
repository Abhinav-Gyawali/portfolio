from django.db import models

# Create your models here.
class ListeningResource(models.Model):
    title = models.CharField(max_length=255)
    product_image = models.TextField()
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    url = models.TextField()
    desc = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)