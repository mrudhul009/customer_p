from rest_framework import serializers
from .models import Customer, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    # prdcts=ProductSerializer(many=True,read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'

