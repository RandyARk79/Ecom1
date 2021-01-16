from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        # field = Product._meta.get_all_field_names()
        fields = ('id', 'name', 'description', 'price', 'image', 'stock', 'category',)
