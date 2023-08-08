from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *



router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('evaluetion', EvaluetionViewSet)


