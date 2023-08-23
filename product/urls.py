from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.CategoryApi.as_view()),
    path('category/<int:category_id>', views.CategoryApi.as_view()),
    path('product/', views.ProductApi.as_view()),
    path('product/<int:product_id>', views.ProductApi.as_view())

]
