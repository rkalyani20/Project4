from django.http import request
from django.shortcuts import render
from rest_framework.validators import ProhibitSurrogateCharactersValidator
from rest_framework.views import APIView
from app4.serializers import CategorySerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import *

class CategoryViews(APIView):

    def get(self, request):
        
        data = CategoryModel.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):

        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    def put(self, request):

        id = request.POST.get('id')
        category = request.POST.get('category')
        data = CategoryModel.object.get(id=id)
        if data:

            data.category = category
            data.save()

            resp={

                'success': 'true',
                'message': '''Category Changed.'''
            }

            return Response(resp, status=status.HTTP_201_CREATED)
        
        resp = {

            'success': 'false',
            'message': 'Something went wrong.'
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    
    def delete(self, request):

        id = CategoryModel.objects.get('id')
        data = CategoryModel.objects.get(id=id).delete()

        resp={

             'success': 'true',
             'message': '''Category Deleted.'''
         }

        return Response(resp,status=status.HTTP_200_OK)
        
        resp = {

                 'success': 'false',
                 'message': 'Something went wrong,'
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

class ProductViews(APIView):

    def get(self, request):

          data = ProductModel.objects.all()
          serializer = ProductSerializer(data, many=True)

          return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if(serializer.is_valid()):

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        id = request.POST.get('id')
        product_name = request.POST.get('product_name')
        product_model_name = request.POST.get('Product_Model_name')
        price = request.POST.get('price')
        product_category = request.POST.get('Product_category')
        data = ProductModel.objects.get(id=id)

        if data:

            data.product_name = product_name
            data.Product_Model_name = product_model_name
            data.price = price
            data.Product_category = product_category
            data.save()

            resp={

                'success': 'true',
                'message': '''Product  Changed.'''
            }

            return Response(resp, status=status.HTTP_201_CREATED)

        resp = {

            'success': 'false',
            'message': 'Something went wrong.'
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self,request):

        id = request.POST.get('id')
        data = ProductModel.object.get(id=id).delete()
        data = ProductModel.objects.get(id=id).delete()

        resp={

            'success': 'true',
            'message': '''Product Deleted.'''

        }

        return Response(resp, status=status.HTTP_200_OK)

        resp = {

            'success': 'false',
            'message': '''Something went wrong.'''
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)