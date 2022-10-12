from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Products
from products import serializers
# Create your views here.

@api_view(['GET'])
def products_list(request):

    product = Products.objects.all()
    serializer = ProductsSerializer(product, many=True)

    return Response(serializer.data)