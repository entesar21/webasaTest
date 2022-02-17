from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from shop_cart.models import Cart
from shop_cart.serializers import CartSerializer

from django.db.models import Sum
from course.models import Course
class CartAPI(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer




