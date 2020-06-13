from django.db import models
# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=25)


  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'cities'



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
