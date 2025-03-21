from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from food.models import Category, Product

User = get_user_model()

class ProductViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998901234567',password='testpass')
        self.staff_user=User.objects.create_superuser(phone_number='+998901234567',password='staffpass')

        self.category = Category.objects.create(name='Pitza')
        self.category = Category.objects.create(name='Ichimliklar')
        self.product1 = Product.objects.create(name='Goshli pitsa',description='mazzali',category=self.category,price=20000)
