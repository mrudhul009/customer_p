from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomerViewSet(APIView):
    def get(self,request):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer(queryset,many=True)
        return Response(serializer_class.data)
    def post(self,request):
        serializer_class=CustomerSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

class ProductViewSet(APIView):
    def get(self,request,pk):
        try:
            obj = Customer.objects.all().filter(id=pk).last()
            print(obj)
            productobj=Product.objects.get(customer=obj)
            print(productobj)
        except Product.DoesNotExist:
            return Response('NO PRODUCTS')
        serializer_class = ProductSerializer(productobj)
        return Response(serializer_class.data)
    def put(self,request,pk):
        queryset=Product.objects.get(pk=pk)
        serializer_class=ProductSerializer(queryset=request.data)
        if serializer_class .is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)
    def post(self,request,pk):
        serializer_class = ProductSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

# setting the products as inactive after 2 months of updation        
@receiver(post_save, sender=Product)
def set_product_inactive(sender, instance, **kwargs):
    if instance.is_active and (timezone.now() - instance.created_at).days >= 60:
        instance.is_active = False
        instance.save()
