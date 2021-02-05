from django.urls import path

from .views import RoleList

urlpatterns = [path("v1/roles/", RoleList.as_view(), name="role=")]
