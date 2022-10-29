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
class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()
    class Meta:
        model = Inventory
        fields = ('id','name', 'description', 'note', 'stock','availability', 'supplier', )
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id','name']