from warnings import filters

from rest_framework.views import APIView, status, Response, Request
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class BaseListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]


# Create your views here.

class BasePagination(PageNumberPagination):
    page_size = 2


# START APIView

# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['categories', 'title']
#
#
# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]

# class CategoryApi(APIView, BasicPagination, BaseFilter, ):
#
#     def get(self, request: Request):
#         categories = Category.objects.all()
#         results = self.paginate_queryset(categories, request, view=self)
#         category_serializer = CategorySerializer(results, many=True)
#         return self.get_paginated_response(category_serializer.data)
#
#     def post(self, request: Request):
#         category_serializer = CategorySerializer(data=request.data)
#         if category_serializer.is_valid():
#             category_serializer.save()
#             return Response('saved')
#         else:
#             return Response(status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request: Request, category_id: int):  # don't need to slash after ID
#         category = Category.objects.get(pk=category_id)
#         category_serializer = CategorySerializer(category, data=request.data)
#         if category_serializer.is_valid():
#             category_serializer.save()
#             return Response(f'{category_serializer.data}==> edited')
#         else:
#             return Response(status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request: Request, category_id: int):  # don't need to slash after ID
#         category = Category.objects.get(pk=category_id)
#         category.delete()
#         return Response('deleted')


# class ProductApi(APIView, BasicPagination, BaseFilter):
#
#     def get(self, request: Request):
#         products = Product.objects.all()
#         results = self.paginate_queryset(products, request, view=self)
#         serializer_product = ProductSerializer(results, many=True)
#         return self.get_paginated_response(serializer_product.data)
#
#     def post(self, request: Request):
#         serializer_product = ProductSerializer(data=request.data)
#         if serializer_product.is_valid():
#             serializer_product.save()
#             return Response('saved')
#
#     def put(self, request: Request, product_id: int):  # don't need to slash after ID
#         product = Product.objects.get(pk=product_id)
#         serializer_product = ProductSerializer(product, data=request.data)
#         if serializer_product.is_valid():
#             serializer_product.save()
#             return Response(f'{serializer_product.data}==> edited')
#         else:
#             return Response(status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request: Request, product_id: int):  # don't need to slash after ID
#         product = Product.objects.get(pk=product_id)
#         product.delete()
#         return Response('deleted')


# END APIView

class ProductListGenericApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = BasePagination
    filterset_fields = ['category', 'title']


class ProductGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListGenericApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = BasePagination
    filterset_fields = ['name']


class CategoryGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
