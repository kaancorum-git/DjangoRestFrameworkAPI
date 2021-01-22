from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
    # fields = ('alis','satis') // belirtilen kisimlari ceker.
    # fields = '__all__' // tum kisimlari ceker.
        fields = '__all__'
