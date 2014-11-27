from django import models

class Picture(models.Model):
    picture=models.ImageField(upload_to='/var/www/backofficeimages/', blank=True, null=True)