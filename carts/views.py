from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *

# Create your views here.
class CartView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            # Your logic here for authenticated users
            cart = Cart.objects.filter(user = user, ordered = False).first() 
            queryset = CartItems.objects.filter(cart=cart) 
            serializer = CartItemsSerializer(queryset, many = True) 
            return Response(serializer.data)
        else:
            return Response({'error': 'User is not authenticated'}, status=401)

    def post(self, request):
        data = request.data
        user = request.user

        # Debugging: Print the received data
        print("Received data:", data)

        try:
            product_id = data.get('products')
            print("Product ID:", product_id)  # Debugging: Print the product ID
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found", code=404)

        cart, created = Cart.objects.get_or_create(user=user, ordered=False)
        price = product.price
        quantity = data.get('quantity', 1)

        cart_item = CartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_item.save()

        # Update total price
        total_price = sum(item.price * item.quantity for item in CartItems.objects.filter(cart=cart))
        cart.total_price = total_price
        cart.save()

        return Response({'success': 'Items added to your cart'}, status=200)

    def put(self, request):
        data = request.data
        cart_item = CartItems.objects.get(id = data.get('id')) 
        cart_item.quantity = data.get('quantity')
        cart_item.save()
        return Response({'Success': 'Items Updated.'}) 
    
    def delete(self, request):
        user = request.user
        data = request.data
        item_id = data.get('id')

        if not item_id:
            return Response({'error': 'ID not provided'}, status=400)

        try:
            cart_item = CartItems.objects.get(id=item_id, cart__user=user, cart__ordered=False)
            cart_item.delete()
            return Response({'success': 'Item deleted successfully'}, status=200)
        except CartItems.DoesNotExist:
            return Response({'error': 'Cart item does not exist'}, status=404)


class OrderAPI(APIView):
    def get(self, request):
        queryset = Orders.objects.filter(user = request.user)
        serializer = OrderSerializer(queryset, many=True) 
        return Response(serializer.data)