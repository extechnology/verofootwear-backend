from django.contrib import admin
from .models import *
import nested_admin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(ProductColors)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")


@admin.register(ProductSizes)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "value")
    search_fields = ("value",)



class VariantImageInline(nested_admin.NestedTabularInline):
    model = VariantImage
    extra = 1
    fields = ("image", "is_primary", "sort_order")




class ProductVariantInline(nested_admin.NestedStackedInline):
    model = ProductVariant
    extra = 1
    show_change_link = True

    fields = (
        "color",
        "size",
        "selling_price",
        "stock",
        "is_active",
    )

    autocomplete_fields = ("color", "size")

    inlines = [VariantImageInline]

    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",)
        }



@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "sub_category",
        "is_new_arrival",
        "created_at",
    )

    list_filter = (
        "category",
        "sub_category",
        "is_new_arrival",
    )

    search_fields = (
        "name",
        "slug",
        "art_number",
    )

    prepopulated_fields = {"slug": ("name",)}

    inlines = [ProductVariantInline]

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "name",
                "slug",
                "art_number",
                "category",
                "sub_category",
            )
        }),
        ("Product Details", {
            "fields": (
                "description",
                "detail_points",
            )
        }),
        ("Status", {
            "fields": ("is_new_arrival",)
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "color",
        "size",
        "selling_price",
        "stock",
        "is_active",
    )

    list_filter = (
        "color",
        "size",
        "is_active",
    )

    search_fields = (
        "product__name",
    )

    autocomplete_fields = (
        "product",
        "color",
        "size",
    )

    inlines = [VariantImageInline]


@admin.register(VariantImage)
class VariantImageAdmin(admin.ModelAdmin):
    list_display = (
        "variant",
        "is_primary",
        "sort_order",
    )

    list_filter = ("is_primary",)



@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "created_at",
        "updated_at",
    )


@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "video_url",
        "created_at",
        "updated_at",
    )


@admin.register(AboutHero)
class AboutHeroAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "created_at",
        "updated_at",
    )