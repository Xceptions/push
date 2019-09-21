from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .models import Builds, Inks, Follows
from .serializers import BuildsSerializer, InksSerializer, FollowsSerializer, UserSerializer, GetUsersSerializer



class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny #this ensures that an anonymous user can register to your site
    ]
    serializer_class = UserSerializer


#===================================================================================================
#suggestfollowers
class GetUsersView(APIView):
    def get(self, request, format=None):
        UserModel = get_user_model()
        getusers = UserModel.objects.all()
        serializer = GetUsersSerializer(getusers, many=True)
        return Response(serializer.data)


#===================================================================================================
#build/
class BuildView(APIView):
    def get(self, request, format=None):
        getbuild = Builds.objects.all()
        serializer = BuildsSerializer(getbuild, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BuildsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        getbuild = Builds.objects.get(pk=pk)
        serializer = BuildsSerializer(getbuild, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        getbuild = Builds.objects.get(pk=pk)
        getbuild.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#==============================================================================================================
#inks/
class InksView(APIView):
    def get_object(self, pk):
        try:
            return Inks.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pk = int(pk)
        getinks = self.get_object(pk)
        serializer = InksSerializer(getinks)
        return Response(serializer.data)

    def post(self, request):
        serializer = InksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = int(pk)
        getinks = self.get_object(pk)
        serializer = InksSerializer(getinks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        getinks = self.get_object(pk)
        getinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#=============================================================================================================
#follow/user
class FollowsView(APIView):
    def get(self, request, following, format=None):
        get_follows = Follows.objects.filter(following=following)
        serializer = FollowsSerializer(get_follows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FollowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)