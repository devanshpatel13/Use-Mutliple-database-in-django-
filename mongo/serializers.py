from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from django.contrib.auth.models import User

class MongoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mongo
        fields = '__all__'

    def create(self, validated_data):
        mongo = Mongo.objects.using("mongo_db").create(
            title = validated_data['title'],
            content = validated_data['content'],
            app_name = validated_data['app_name']
        )
        return mongo



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'