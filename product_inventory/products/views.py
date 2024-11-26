from django.http import JsonResponse
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

# GET: Retrieve all products
def get_products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

# GET: Retrieve a single product by ID
def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return JsonResponse({
            "id": product.id,
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "mrp": str(product.mrp),
            "distributor_price": product.distributor_price
        })
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

# POST: Add a new product
@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            product = Product.objects.create(
                product_id=data['product_id'],
                name=data['name'],
                description=data['description'],
                mrp=data['mrp'],
                distributor_price=data['distributor_price']
            )
            return JsonResponse({
                "id": product.id,
                "product_id": product.product_id,
                "name": product.name,
                "description": product.description,
                "mrp": str(product.mrp),
                "distributor_price": product.distributor_price
            }, status=201)
        except KeyError:
            return JsonResponse({"error": "Invalid data"}, status=400)

# PUT: Update an existing product by ID
@csrf_exempt
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if request.method == 'PUT':
            data = json.loads(request.body)
            product.product_id = data.get('product_id', product.product_id)
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.mrp = data.get('mrp', product.mrp)
            product.distributor_price = data.get('distributor_price', product.distributor_price)
            product.save()
            return JsonResponse({
                "id": product.id,
                "product_id": product.product_id,
                "name": product.name,
                "description": product.description,
                "mrp": str(product.mrp),
                "distributor_price": product.distributor_price
            })
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

# DELETE: Remove a product by ID
@csrf_exempt
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return JsonResponse({"message": "Product deleted"})
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
