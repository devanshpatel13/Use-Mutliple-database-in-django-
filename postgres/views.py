from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.


class PostgresView(generics.ListCreateAPIView):
    queryset = Postgres.objects.using("postgres_db").all()
    serializer_class = PostgresSerializers

    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = self.get_serializer(data=payload, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(using='mongo_db')

        return Response("data")

class PostgresUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postgres.objects.using("postgres_db").all()
    serializer_class = PostgresSerializers
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()

        payload = request.data
        instance = Postgres.objects.using("postgres_db").get(pk=kwargs['pk'])
        # import pdb;pdb.set_trace()
        serializer = self.serializer_class(data=payload, context={'request': request})
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        instance = serializer.update(instance, validated_data)
        # import pdb;pdb.set_trace()
        return instance



