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
 