from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
