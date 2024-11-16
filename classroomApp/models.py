from django.db import models #type: ignore

# Create your models here.
class Room(models.Model):
    # host= models.CharField(max_length=100)
    # topic = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # capacity = models.IntegerField(default=0),
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
