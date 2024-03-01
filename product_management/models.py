from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


# Represents the definition of an attribute(param)
class AttributeDefinition(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Represents the type of a product
class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Represents products
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey('ProductType', verbose_name=_("Product Type"), on_delete=models.DO_NOTHING)
    title = models.CharField(_("Product title"), max_length=50)
    description = models.TextField(null=True, blank=True)
    assigned_attributes = models.ManyToManyField(AttributeDefinition, through='ProductAttribute', verbose_name=_("Assigned attributes"))
    favorites = models.ManyToManyField(User, through='Favorite', related_name='favorite_products')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


# Represents attributes assigned to a product
class ProductAttribute(models.Model):
    id = models.BigAutoField(primary_key=True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(AttributeDefinition, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('product', 'attribute')

    def __str__(self):
        return f"{self.product.title} - {self.attribute.name}: {self.value}"


# Represents a user's favorite product
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product') 

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

