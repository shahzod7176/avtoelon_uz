from rest_framework import serializers
from apps.models import Category, Product, CharactererAvto, ElonCharacter, Parametres, Type, Measure, ParametresItem, Files, \
    ElonFiles, Status, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'year', 'engine_size', 'mileage', 'transmission', 'price', 'category']


class CharactererAvtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharactererAvto
        fields = ['id', 'user_id', 'title', 'description', 'status', 'price']


class ElonCharacterSerializer(serializers.ModelSerializer):
    parametres = serializers.StringRelatedField()
    parametres_item = serializers.StringRelatedField()

    class Meta:
        model = ElonCharacter
        fields = ['id', 'elon', 'parametres', 'parametres_item', 'parametres_value']


class ParametresSerializer(serializers.ModelSerializer):
    measure = serializers.StringRelatedField()

    class Meta:
        model = Parametres
        fields = ['id', 'name', 'param_type', 'measure']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'code']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'name', 'short_name']


class ParametresItemSerializer(serializers.ModelSerializer):
    parametres = serializers.StringRelatedField()
    file = serializers.StringRelatedField()

    class Meta:
        model = ParametresItem
        fields = ['id', 'parametres', 'name', 'value', 'file']


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'file']


class ElonFilesSerializer(serializers.ModelSerializer):
    elon = serializers.StringRelatedField()
    file = serializers.StringRelatedField()

    class Meta:
        model = ElonFiles
        fields = ['id', 'elon', 'file']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'description', 'code']


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'photo']
