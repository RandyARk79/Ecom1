from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        # field = Category._meta.get_all_field_names()
        fields = ('name', 'description')
