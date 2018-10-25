from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserDetailSerializer
from .models import  UserDetail
import requests
from . pagination import PostLimitOffsetPagination,PostPageNumberPagination

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user details."""
        serializer.save()

class GetList(generics.ListAPIView):
    """ 
    This class to get all user details at once
    based on filter that are we apply

    """
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    pagination_class = PostPageNumberPagination
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        if self.request.method=='GET':
            name = self.request.GET.get('name')
            sort = self.request.GET.get('sort')

            if name is not None:
                return UserDetail.objects.filter(first_name=name).order_by(sort)

            else:
                return UserDetail.objects.all()
      
        
class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    """
    This class handles the http GET, PUT and DELETE requests.
    """

    serializer_class = UserDetailSerializer
    queryset = UserDetail.objects.all()

    


