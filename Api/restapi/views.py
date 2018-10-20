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
    """ This class to get all user details at once"""
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

    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = UserDetailSerializer
    queryset = UserDetail.objects.all()

    



#     def query_paramametrs(self):
#         name = request.Get['name']
#         sort  = request.Get['age']
#         limit = request.Get['limit']
#         page =  request.Get['page']

#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")




# def get_queryset(self):
#         if self.request.method == 'GET':
#             print('GET line 26')
#             print(self.request.GET.get('name'))
#         elif self.request.method == 'POST':
#             print('POST ')



    # def get_queryset(self):
    #     name = request.Get.get('name')
    #     sort  = request.Get.get('age')
    #     limit = request.Get.get('limit')
    #     page =  request.Get.get('page')

    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    #     print(name)

# def get_detail(request):
#     name = request.GET.get('name')
#     age  = request.GET.get('age')
#     limit = request.Get.get('limit')
#     page = request

#     context = {
#         'verification_code': verification_code,
#         'userid': verification_url,
#     }

#     return render_to_response('callback.html', context, context_instance=RequestContext(request))


    # def get_queryset(self):
    #     if self.request.method == 'GET':
    #         queryset = UserDetail.objects.all()
    #         name = self.request.GET.get('name', None)
    #         if first_name is not None:
    #             queryset = queryset.filter(first__name=name).order_by('-age')
    #         return queryset 



    #  def get_queryset(self):
    #     queryset = Passenger.objects.all()
    #     workspace = self.request.query_params.get('workspace')
    #     airline = self.request.query_params.get('airline')

    #     if workspace:
    #         queryset = queryset.filter(workspace_id=workspace)
    #     elif airline:
    #         queryset = queryset.filter(workspace__airline_id=airline)

    #     return queryset