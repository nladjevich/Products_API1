from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import ProductsSerializer
from .models import Products
from products import serializers
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        product = Products.objects.all()
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, stuatus=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)