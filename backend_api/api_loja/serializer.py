from rest_framework import serializers
from .models import Category, Product, Evaluetion


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['describe']

### --- ###
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
### --- ###
class EvaluetionSerializer(serializers.ModelSerializer):

    class Meta:
        write = {
            'email': {'write_only': True}
        }
        model = Evaluetion
        fields = '__all__'
