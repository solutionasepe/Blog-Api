from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Example
from .serializers import PostSerializer, UserSerializer, ExampleSerializer
from rest_framework import generics, status, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorOrReadOnly
from django.utils.decorators import method_decorator
from braces.views import CsrfExemptMixin

# Create your views here.
# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthorOrReadOnly])
# def Posting(request):
#     if request.method == 'POST':
#         serializer = PostSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#     else:
#         try:
#             posts = Post.objects.all()
#         except Post.DoesNotExist:
#             return Response(status= status.HTTP_404_NOT_FOUND)

#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)



class PostViewSet(viewsets.ModelViewSet, CsrfExemptMixin):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class Exampleview( generics.ListAPIView, CsrfExemptMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer