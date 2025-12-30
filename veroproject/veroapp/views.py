from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductColorsViewSet(viewsets.ModelViewSet):
    queryset = ProductColors.objects.all()
    serializer_class = ProductColorsSerializer


class ProductSizesViewSet(viewsets.ModelViewSet):
    queryset = ProductSizes.objects.all()
    serializer_class = ProductSizesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class VariantImageViewSet(viewsets.ModelViewSet):
    queryset = VariantImage.objects.all()
    serializer_class = VariantImageSerializer


class HeroImageViewSet(viewsets.ModelViewSet):
    queryset = HeroImage.objects.all()
    serializer_class = HeroImageSerializer


class YoutubeVideoViewSet(viewsets.ModelViewSet):
    queryset = YoutubeVideo.objects.all()
    serializer_class = YoutubeVideoSerializer   


class AboutHeroViewSet(viewsets.ModelViewSet):
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializer
    