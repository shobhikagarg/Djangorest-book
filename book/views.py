#noinspection PyUnresolvedReferences
from django.shortcuts import render
#noinspection PyUnresolvedReferences
from django.http import Http404
from rest_framework import status, generics
#noinspection PyUnresolvedReferences
from rest_framework.response import Response
#noinspection PyUnresolvedReferences
from rest_framework.views import APIView
#noinspection PyUnresolvedReferences
from rest_framework import mixins
#noinspection PyUnresolvedReferences
from .models import Author,Book,Comment
#noinspection PyUnresolvedReferences
from .serializers import BookSerializer,AuthorSerializer,CommentSerializer
from django_filters import rest_framework as filters
#noinspection PyUnresolvedReferences
from rest_framework.filters import SearchFilter
#noinspection PyUnresolvedReferences
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'

class Bookgenericview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    lookup_field = 'id'


    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

class AuthorgenericView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend,SearchFilter)
    search_fields = ['name']
    pagination_class = LargeResultsSetPagination

class CommentAPIView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class CommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()