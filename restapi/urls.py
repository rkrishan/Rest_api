from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView 
from .views import GetList
      

urlpatterns = [
    path('createdetail/', CreateView.as_view(),name="create"),
    path('users/', GetList.as_view(),name="getdetail"),
    re_path(r'^users/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
    
    
]
urlpatterns = format_suffix_patterns(urlpatterns)