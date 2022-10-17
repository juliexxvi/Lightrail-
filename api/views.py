from rest_framework.response import Response
from rest_framework.decorators import api_view
from zipfile import ZipFile
from . import utils
from base.models import Stop, Trip, StopTime

@api_view(['POST'])
def upload_GTFS_file(request):
    file_obj = request.data['file']
    
    try:
        with ZipFile(file_obj, 'r') as zip:
            utils.add_to_database_in_order(zip)
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

    kwargs = {'stop__stop_id': stop_id, f'trip__service__{day}': 1}
    stop_times = list(StopTime.objects.filter(**kwargs).order_by('departure_time'))
    schedules = []
    for stop_time in stop_times:
        schedule = {
            'arrival_time': stop_time.arrival_time,
            'departure_time': stop_time.departure_time,
            'stop_headsign': stop_time.stop_headsign,
            'trip_headsign': stop_time.trip.trip_headsign,
            'route_direction': stop_time.trip.route_direction,
        }
        schedules.append(schedule)
    data = {
        'stop_id': stop_id,
        'stop_name': stop.stop_name,
        'platform_code': stop.platform_code,
        'wheelchair_boarding': stop.wheelchair_boarding,
        'schedules': schedules,
    }
    
    return Response(data)

@api_view(['GET'])
def get_trips(request):
    trips = Trip.objects.all()
    uri = request.build_absolute_uri()
    links = map(lambda trip: f'{uri}/{trip.trip_id}', trips)
    return Response(links)
