from rest_framework import serializers
from .models import Category, Product, Evaluetion


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fiels = '__all__'

### --- ###
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
### --- ###
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        write = {
            'email': {'write_only': True}
        }
        model = Evaluetion
        fields = '__all__'
