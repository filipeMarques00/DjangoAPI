from rest_framework import serializers
from groups import models

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groups
        fields = '__all__'