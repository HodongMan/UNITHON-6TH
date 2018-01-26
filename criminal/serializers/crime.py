from rest_framework import serializers

from ..models import Crime

class CrimeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Crime
        fields = (
            'pk',
            'year',
            'area',
            'location',
            'type',
            'occur',
            'arrest'
        )