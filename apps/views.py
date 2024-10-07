from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from apps.models import Product, Category


def home_view(request):
    return render(request, 'apps/base.html')


def redirect_to_products(request):
    return redirect('product-list')


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        category_slug = self.request.GET.get('category')
        queryset = super().get_queryset().select_related('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product/product-detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView

from apps.models import User, Measure, CharactererAvto, Parametres, Files, ParametresItem, ElonCharacter, ElonFiles
from apps.serializers import UserSerializer, FilesSerializer, MeasureSerializer, ParametresSerializer, \
    ParametresItemSerializer, ElonCharacterSerializer, ElonFilesSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return User.objects.all()


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        return User.objects.create_user(data['username'], data['email'], data['password'])


class UpdateUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        data = serializer.validated_data
        return User.objects.update_user(data['username'], data['email'], data['password'])


class DeleteUserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        data = request.data
        if data['username']:
            del data['username', 'email', 'password']


class FilesListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = FilesSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Files.objects.all()


class CharacterAutoApiListView(ListAPIView):
    queryset = CharactererAvto.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return CharactererAvto.objects.all()


class MeasureListApiView(ListAPIView):  # noqa
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Measure.objects.all()


class ParameterListApiView(ListAPIView):  # noqa
    queryset = Parametres.objects.all()
    serializer_class = ParametresSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Parametres.objects.all()


class ParametersItemListApiView(ListAPIView):
    queryset = Parametres.objects.all()
    serializer_class = ParametresItemSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return ParametresItem.objects.all()


class ElonCharacterListApiView(ListAPIView):
    queryset = ElonCharacter.objects.all()
    serializer_class = ElonCharacterSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return ElonCharacter.objects.all()


class ElonFilesListApiView(ListAPIView):
    queryset = ElonFiles.objects.all()
    serializer_class = ElonFilesSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return ElonFiles.objects.all()
