from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from account.api.permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import *
from account.api.serializers import PackageSerializer, UserSerializer, CategorySerializer, ImageSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAdminUser,]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PackageViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class UploadImageAdminView(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, ]
#     permission_classes = [IsAdminUser,]
#     serializer_class = UploadImageSerializer
#     queryset = User.objects.all()


class UploadImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ImageSerializer
    queryset = UploadImage.objects.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)