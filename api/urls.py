from django.urls import path, re_path
from . import views

urlpatterns = [
    path('stops', views.get_stops),
    path('stops/<str:stop_id>', views.get_stop_schedules),
    path('upload', views.upload_GTFS_file),
]
