from django.urls import path, include
from . import views
urlpatterns = [
    path('product/', views.ProductListGenericApiView.as_view()),
    path('product/<pk>', views.ProductGenericApiView.as_view()),
    path('category/', views.CategoryListGenericApiView.as_view()),
    path('category/<pk>', views.CategoryListGenericApiView.as_view()),

]
