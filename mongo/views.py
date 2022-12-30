from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework import generics


# Create your views here.


class MongoView(generics.ListCreateAPIView):
    queryset = Mongo.objects.using('mongo_db').all()
    serializer_class = MongoSerializers


    def post(self, request, *args, **kwargs):
        payload  = request.data
        serializer = self.get_serializer(data=payload, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(using ='mongo_db')

        return Response("data")


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


    def create(self, request, *args, **kwargs):
        return Response("data")