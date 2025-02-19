# api/utils/serializsers/pager.py

from rest_framework import serializers

from . import models


class PagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"
