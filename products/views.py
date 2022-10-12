from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import ProductsSerializer
from .models import Products
from products import serializers
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