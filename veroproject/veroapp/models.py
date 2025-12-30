from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class ProductColors(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_colors/', blank=True, null=True)
    code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductSizes(models.Model):
    value = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value



class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    art_number = models.CharField(max_length=100)
    description = models.TextField()
    detail_points = models.TextField(blank=True, null=True)
    is_new_arrival = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )
    color = models.ForeignKey(ProductColors, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSizes, on_delete=models.CASCADE)


    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('product', 'color', 'size')
        indexes = [
            models.Index(fields=['product', 'color']),
            models.Index(fields=['product', 'size']),
        ]

    def __str__(self):
        return f"{self.product.name} | {self.color} | {self.size}"



class VariantImage(models.Model):
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/variants/')
    is_primary = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.variant.product.name} | {self.variant.color} | {self.variant.size}"




class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_carousel/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)


class YoutubeVideo(models.Model):
    image = models.ImageField(upload_to='youtube_videos/')
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)


class AboutHero(models.Model):
    image = models.ImageField(upload_to='about/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.image)



