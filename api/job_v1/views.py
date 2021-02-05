from rest_framework import generics

from jobs.models import Role
from api.job_v1.serializers import RoleSerializer


class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
