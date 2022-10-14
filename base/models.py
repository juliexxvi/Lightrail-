from django.db import models

# Create your models here.

class Agency(models.Model):
    agency_id = models.CharField(max_length=200)
    agency_name = models.CharField(max_length=200)
    agency_url = models.CharField(max_length=200)
    agency_timezone = models.CharField(max_length=200)
    agency_lang = models.CharField(max_length=200)
    agency_phone = models.CharField(max_length=200)

class CalendarDate(models.Model):
    service_id = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    exception_type = models.IntegerField()

class Calendar(models.Model):
    service_id = models.CharField(max_length=200)
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

class Route(models.Model):
    route_id = models.CharField(max_length=200)
    agency_id = models.CharField(max_length=200)
    route_short_name = models.CharField(max_length=200)
    route_long_name = models.CharField(max_length=200)
    route_desc = models.CharField(max_length=200)
    route_type = models.CharField(max_length=200)
    route_colour = models.CharField(max_length=200)
    route_text_colour = models.CharField(max_length=200)

class Shape(models.Model):
    shape_id = models.CharField(max_length=200)
    shape_pt_lat = models.CharField(max_length=200)
    shape_pt_lon = models.CharField(max_length=200)
    shape_pt_sequence = models.CharField(max_length=200)
    shape_dist_traveled = models.CharField(max_length=200)

class StopTime(models.Model):
    trip_id = models.CharField(max_length=200)
    arrival_time = models.CharField(max_length=200)
    departure_time = models.CharField(max_length=200)
    stop_id = models.CharField(max_length=200)
    stop_sequence = models.IntegerField()
    stop_headsign = models.CharField(max_length=200)
    pickup_type = models.IntegerField()
    drop_off_type = models.IntegerField()
    shape_distance_traveled = models.CharField(max_length=200)
    timepoint = models.IntegerField()
    stop_note_id = models.CharField(max_length=200)

class Stop(models.Model):
    stop_id = models.CharField(max_length=200)
    stop_name = models.CharField(max_length=200)
    stop_lat = models.CharField(max_length=200)
    stop_lon = models.CharField(max_length=200)
    location_type = models.IntegerField()
    parent_station = models.CharField(max_length=200)
    wheelchair_boarding = models.IntegerField()
    platform_code = models.CharField(max_length=200)

class Trip(models.Model):
    route_id = models.CharField(max_length=200)
    service_id = models.CharField(max_length=200)
    trip_id = models.CharField(max_length=200)
    trip_headsign = models.CharField(max_length=200)
    direction_id = models.IntegerField()
    block_id = models.CharField(max_length=200)
    shape_id = models.CharField(max_length=200)
    wheelchair_accessible = models.IntegerField()
    trip_note_id = models.CharField(max_length=200)
    route_direction = models.CharField(max_length=200)

class Note(models.Model):
    note_id = models.CharField(max_length=200)
    note_text = models.CharField(max_length=200)
