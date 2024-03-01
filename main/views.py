from django.shortcuts import render
from product_management.models import Product, ProductAttribute
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from product_management.models import Product, Favorite
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError


# View for the home page
def home(request):
    
    products = Product.objects.all()
    product_attributes = ProductAttribute.objects.select_related('product', 'attribute').all()

    context = {
        'products': products,
        'product_attributes': product_attributes
    }

    return render(request, "index.html", context)


# View to toggle favorite status for a product
@login_required
def toggle_favorite(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    # If the favorite already exists, delete it (toggle)
    if not created:
        favorite.delete()

    return redirect('home')


# View to display user's favorite products
@login_required
def favorites(request):
 
    favorite_products = request.user.favorite_products.all()
    
    context = {'favorite_products': favorite_products}

    return render(request, 'favorites.html', context)


# View to compare selected products
@csrf_exempt
def compare_products(request):

    if request.method == 'POST':

        product_ids = request.POST.getlist('compare')

        # Check if the number of selected products exceeds the limit
        if len(product_ids) > 4 :
            raise ValidationError('Exceeded maximum number of products for comparison')
        
        selected_products = Product.objects.filter(id__in=product_ids)
        selected_product_attributes = ProductAttribute.objects.filter(product__in=product_ids)

        context = {
            'selected_products': selected_products, 
            'selected_product_attributes': selected_product_attributes
                    }
        
    return render(request, 'compare.html', context)