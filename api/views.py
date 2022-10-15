from rest_framework.response import Response
from rest_framework.decorators import api_view
from zipfile import ZipFile
import csv
from io import TextIOWrapper
from . import utils
from base.models import Stop, Trip, StopTime, Calendar

@api_view(['POST'])
def upload_GTFS_file(request):
    file_obj = request.data['file']
    
    try:
        with ZipFile(file_obj, 'r') as zip:
            for csv_name in zip.namelist():
                with zip.open(csv_name, 'r') as file:
                    reader = csv.reader(TextIOWrapper(file, 'utf-8'))
                    next(reader, None) # skip header
                    for row in reader:
                        utils.add_to_database(csv_name, row)
        return Response(data={'message': 'Process file successfully!'}, status=201)
    except Exception as e:
        return Response(data={'message': 'Something went wrong', 'error': str(e)}, status=415)
    
@api_view(['GET'])
def get_stops(request):
    stops = Stop.objects.all()
    uri = request.build_absolute_uri()
    links = map(lambda stop: f'{uri}/{stop.stop_id}', stops)
    return Response(links)

@api_view(['GET'])
def get_stop_schedules(request, stop_id):
    day = request.GET.get('day')
    day_of_weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    if day is None or day not in day_of_weeks:
        data = {
            'message': f'Invalid query param, param "day" must be one of these: {", ".join(day_of_weeks)}'
        }
        return Response(data, status=400)

    try:
        stop = Stop.objects.get(stop_id=stop_id)
    except Stop.DoesNotExist:
        data = {
            'message': f'Cannot find stop_id {stop_id}'
        }
        return Response(data, status=400)

    stop_times = StopTime.objects.filter(stop_id=stop_id)
    trip_ids = list(stop_times.values_list('trip_id', flat=True).distinct())
    trips = Trip.objects.filter(trip_id__in=trip_ids)

    service_ids = list(trips.values_list('service_id', flat=True).distinct())
    kwargs = {
        'service_id__in': service_ids,
        day: 0,
    }
    valid_service_ids = list(Calendar.objects.filter(**kwargs).values_list('service_id', flat=True))
    # Todo: join multiple tables
    
    return Response()
