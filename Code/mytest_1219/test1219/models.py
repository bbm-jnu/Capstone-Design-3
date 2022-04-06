from django.db import models

class Wifi_2018103297(models.Model):
    installLocationDetail = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    addressDong = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name_text

