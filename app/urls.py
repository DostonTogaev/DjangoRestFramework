from django.urls import path
from app.views import  CategiryAPIView

urlpatterns = [
    
    path('', CategiryAPIView.as_view(), name='category' )
]