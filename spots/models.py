from django.db import models

# Create your models here.


class Spot(models.Model):
    idn = models.IntegerField(unique = True)
    name = models.CharField(max_length = 200)
    description= models.CharField(max_length = 1000)
    
    tourist_weigth = models.IntegerField()
    urbex_weigth = models.IntegerField()
    walk_weight = models.IntegerField()
    
    class Meta:
        ordering = ('idn',)
    
    
    # TO BE COMPLETED -> Other definition, save, create ...