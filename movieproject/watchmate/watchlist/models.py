from django.db import models



class Streamplatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=500)
    website=models.URLField(max_length=200)
    def __str__(self):
        return self.name
# Create your models here.
class Watchlist(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=400)
    platform=models.ForeignKey(Streamplatform,on_delete=models.CASCADE,related_name="Watchlist")
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name    
    
