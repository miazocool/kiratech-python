from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Inventory, Supplier


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class InventorySerializer(serializers.HyperlinkedModelSerializer):
    # supplier = serializers.StringRelatedField(many=True)
    class Meta:
        model = Inventory
        fields = ['id','name', 'availability', 'supplier']

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id','name']