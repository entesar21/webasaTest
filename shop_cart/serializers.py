from rest_framework import serializers

from shop_cart.models import Cart
from users.models import User
from course.models import Course
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_title', 'course_category','course_discounted_price', 'course_image')

class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=False)
    product = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ('cart_id', 'product', 'created_at', 'updated_at')
        # depth = 2