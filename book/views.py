from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, \
    DestroyModelMixin, RetrieveModelMixin


class CategoryGenericsViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookGenericsViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class CategoryGenericsViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin,
#                               DestroyModelMixin, RetrieveModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryCreateAPIView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryListAPIView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#
# class CategoryUpdateAPIView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryDestroyAPIView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryRetrieveAPIView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
