from rest_framework import serializers

from .models import Hero


class HeroSerializer(serializers.ModelSerializer):
    
    
    #4. Nested Class
    class Meta:
        model = Hero
        fields = ('fullname','alias')
    pass
