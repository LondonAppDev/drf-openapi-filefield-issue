from django.db import models


class Profile(models.Model):
    image = models.FileField(upload_to='uploads/%Y/%m/%d/')
