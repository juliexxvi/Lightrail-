from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', views.upload_GTFS_file),
]
