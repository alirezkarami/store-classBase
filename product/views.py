from rest_framework.views import APIView, status, Response, Request
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import ListAPIView


# Create your views here.
class BasicPagination(PageNumberPagination):
    pass


class CategoryApi(APIView, BasicPagination):

    def get(self, request: Request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return self.get_paginated_response(category_serializer.data)

    def post(self, request: Request):
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response('saved')
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    # dont need slash

    def put(self, request: Request, category_id: int):  # don't need slash after ID
        category = Category.objects.get(pk=category_id)
        category_serializer = CategorySerializer(category, data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(f'{category_serializer.data}==> edited')
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, category_id: int):  # don't need slash after ID
        category = Category.objects.get(pk=category_id)
        category.delete()
        return Response('deleted')


class ProductApi(APIView):
    def get(self, request: Request):
        products = Product.objects.all()
        serializer_product = ProductSerializer(products, many=True)
        return Response(serializer_product.data, status.HTTP_201_CREATED)

    def post(self, request: Request):
        serializer_product = ProductSerializer(data=request.data)
        if serializer_product.is_valid():
            serializer_product.save()
            return Response('saved')

    def put(self, request: Request, product_id: int):  # don't need slash after ID
        product = Product.objects.get(pk=product_id)
        serializer_product = ProductSerializer(product, data=request.data)
        if serializer_product.is_valid():
            serializer_product.save()
            return Response(f'{serializer_product.data}==> edited')
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, product_id: int):  # don't need slash after ID
        product = Product.objects.get(pk=product_id)
        product.delete()
        return Response('deleted')
