from rest_framework import viewsets
from groups.api import serializers
from groups import models

class GroupsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupsSerializer
    queryset = models.Groups.objects.all()