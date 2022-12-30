from rest_framework import serializers
from .models import *
from rest_framework.response import Response



class PostgresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Postgres
        fields = '__all__'

    def create(self, validated_data):
        mongo = Postgres.objects.using("postgres_db").create(
            name = validated_data['name'],
            numbers = validated_data['numbers']
        )
        return mongo
    # #
    def update(self, instance, validated_data):
        # import pdb;pdb.set_trace()
        instance.name = validated_data['name']
        instance.number = validated_data['numbers']
        instance.save()
        return instance
    #
