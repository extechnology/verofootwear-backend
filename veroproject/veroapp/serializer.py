from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from .models import *
from django.db.models import Min
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
    

class ProductColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColors
        fields = '__all__'
    

class ProductSizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizes
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    sub_category_name = serializers.CharField(source='sub_category.name', read_only=True)
    image = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, obj):
        primary_image = VariantImage.objects.filter(
            variant__product=obj,
            is_primary=True
        ).order_by("sort_order").first()

        if primary_image:
            return primary_image.image.url

        fallback_image = VariantImage.objects.filter(
            variant__product=obj
        ).order_by("sort_order").first()

        if fallback_image:
            return fallback_image.image.url

        return None

    def get_price(self, obj):
        """
        Returns the lowest selling price among active variants
        """
        price = obj.variants.filter(
            is_active=True
        ).aggregate(
            min_price=Min("selling_price")
        )["min_price"]

        return price




class ProductVariantSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(source="color.name", read_only=True)
    color_code = serializers.CharField(source="color.code", read_only=True)
    size_value = serializers.CharField(source="size.value", read_only=True)

    variant_image = serializers.SerializerMethodField()
    variant_images = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = "__all__"

    def get_variant_image(self, obj):
        """
        Returns PRIMARY image → fallback first image → None
        """
        request = self.context.get("request")

        image = (
            obj.images.filter(is_primary=True).first()
            or obj.images.first()
        )

        if image and request:
            return request.build_absolute_uri(image.image.url)

        return None

    def get_variant_images(self, obj):
        """
        Returns all images (gallery)
        """
        request = self.context.get("request")
        if not request:
            return []

        return [
            request.build_absolute_uri(img.image.url)
            for img in obj.images.all()
        ]



class VariantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantImage
        fields = '__all__'  


class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = '__all__'


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'


class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = '__all__'
