from rest_framework import serializers
from spots.models import Spot

# Create your serializers here

class SpotSerializer(serializers.Serializer):
        
        
        class Meta: 
            model = Spot
            fields = ('s_name', 's_description', 'longitude', 'latitude', )
    
