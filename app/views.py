from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from app.models import  Category


class CategiryAPIView(APIView):


    def get(self, request):
        category_data = [{
            'title': category.title,
            'image': category.image.url if category.image else None,

        }
        for category in Category.objects.all()]     
        return Response (category_data, status=status.HTTP_200_OK)

