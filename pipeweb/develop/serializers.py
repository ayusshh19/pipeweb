from rest_framework import serializers

from develop.models import products

class prodt(serializers.ModelSerializer):
    class Meta:
        model=products
        fields='__all__'