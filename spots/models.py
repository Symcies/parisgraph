from django.db import models

# Create your models here.


class Spot(models.Model):
    idn = models.IntegerField(unique = True)
    s_name = models.CharField(max_length = 200)
    s_description = models.CharField(max_length = 1000)
    
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    tourist_weight = models.IntegerField()
    urbex_weight = models.IntegerField()
    walk_weight = models.IntegerField()
    
    def reward(self, tourist_, urbex_, walk_):
        user_reward = tourist_ * self.tourist_weight + urbex_ * self.urbex_weight + walk_ * self.walk_weight
        return user_reward
    
    class Meta:
        ordering = ('idn',)
    
    
    # TO BE COMPLETED -> Other definition, save, create ...
    #### ADD THE FUNCTION TO CALCTULATE THE WEIGTH BASED ON USER PREFERENCES