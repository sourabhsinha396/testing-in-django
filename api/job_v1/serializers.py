from rest_framework import serializers
from jobs.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["title", "slug"]
