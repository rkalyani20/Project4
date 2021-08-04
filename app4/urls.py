from django.urls import path,include
from .views import *

urlpatterns = [
    path('category-view/', CategoryViews.as_view()),
    path('product-view/', ProductViews.as_view()),
    
    
]
