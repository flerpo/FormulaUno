from django.db import models


# Create your models here.
class Tracks(models.Model):
    trackId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/tracks")

    def __str__(self):
        return self.name + ' ' + self.location


class Results(models.Model):
    user = models.CharField(max_length=30)
    registered_time = models.CharField(max_length=20)
    updated_time = models.DateTimeField()
    user_image = models.ImageField(upload_to="images/userImages")
    trackId = models.IntegerField
