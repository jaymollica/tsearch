from django.db import models
# Create your models here.

class Color(models.Model):
  name = models.CharField(max_length=100)
  hex_str = models.CharField(max_length=6)

  def __str__(self):
    return self.name

class Country(models.Model):
  name = models.CharField(max_length=100, unique=True)
  svg = models.CharField(max_length=100,null=True)

  def __str__(self):
    return self.name

class Medium(models.Model):
  medium = models.CharField(max_length=100, unique=True)
  url = models.CharField(max_length=100,null=True)

  def __str__(self):
    return self.medium

class Artwork(models.Model):
  title = models.CharField(max_length=100)
  url = models.CharField(max_length=100)
  artist = models.CharField(max_length=100, default="")
  date_created = models.DateTimeField(null=True)
  country = models.ForeignKey("Country")
  medium = models.ForeignKey("Medium")
  #valid_url = models.BooleanField()
  
  #color = models.ForeignKey("Color", related_name="dominant_color")

  def __str__(self):
    return self.title

