from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_mod_date = models.DateTimeField(auto_now=True)
