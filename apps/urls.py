from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from apps.views import (
    home_view,
    redirect_to_products,
    ProductListView,
    ProductDetailView,
    UserListApiView,
    CreateUserView,
    UpdateUserView,
    DeleteUserView,
    FilesListApiView,
    CharacterAutoApiListView,
    MeasureListApiView,
    ParameterListApiView,
    ParametersItemListApiView,
    ElonCharacterListApiView,
    ElonFilesListApiView
)

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('redirect/', redirect_to_products, name='redirect-to-products'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),

    path('api/users/', UserListApiView.as_view(), name='user-list-api'),
    path('api/users/create/', CreateUserView.as_view(), name='user-create-api'),
    path('api/users/update/<int:pk>/', UpdateUserView.as_view(), name='user-update-api'),
    path('api/users/delete/<int:pk>/', DeleteUserView.as_view(), name='user-delete-api'),

    path('api/files/', FilesListApiView.as_view(), name='files-list-api'),

    path('api/character-avto/', CharacterAutoApiListView.as_view(), name='character-avto-list-api'),

    path('api/measures/', MeasureListApiView.as_view(), name='measure-list-api'),
    path('api/parameters/', ParameterListApiView.as_view(), name='parameter-list-api'),
    path('api/parameter-items/', ParametersItemListApiView.as_view(), name='parameter-item-list-api'),

    path('api/elon-characters/', ElonCharacterListApiView.as_view(), name='elon-character-list-api'),
    path('api/elon-files/', ElonFilesListApiView.as_view(), name='elon-files-list-api'),
]
