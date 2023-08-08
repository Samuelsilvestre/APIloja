from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import *
from .models import *

### --- ###
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    

### --- ###
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


### --- ###
class EvaluetionViewSet(viewsets.ModelViewSet):
    queryset = Evaluetion.objects.all()
    serializer_class = EvaluetionSerializer
