from django.db import models

# Create your models here.
class WeatherCollection(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    temperature = models.FloatField()
    weather_description = models.CharField(max_length=100)

    def __str__(self):
        return "{}, {} {} C".format(*(self.city, self.country,
        self.temperature))
