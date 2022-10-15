from base.models import Agency, CalendarDate, Calendar, Route, Shape, StopTime, Stop, Trip, Note

def add_to_database(filename, row):
    try:
        match filename:
            case 'agency.txt':
                data = {
                    'agency_id': row[0],
                    'agency_name': row[1],
                    'agency_url': row[2],
                    'agency_timezone': row[3],
                    'agency_lang': row[4],
                    'agency_phone': row[5],
                }
                Agency.objects.update_or_create(agency_id=data['agency_id'], defaults=data)

            case 'calendar_dates.txt':
                data = {
                    'service_id': row[0],
                    'date': row[1],
                    'exception_type': row[2],
                }
                CalendarDate.objects.update_or_create(service_id=data['service_id'], date=data['date'], defaults=data)

            case 'calendar.txt':
                data = {
                    'service_id': row[0],
                    'monday': row[1],
                    'tuesday': row[2],
                    'wednesday': row[3],
                    'thursday': row[4],
                    'friday': row[5],
                    'saturday': row[6],
                    'sunday': row[7],
                    'start_date': row[8],
                    'end_date': row[9]
                }
                Calendar.objects.update_or_create(service_id=data['service_id'], defaults=data)

            case 'routes.txt':
                data = {
                    'route_id': row[0],
                    'agency_id': row[1],
                    'route_short_name': row[2],
                    'route_long_name': row[3],
                    'route_desc': row[4],
                    'route_type': row[5],
                    'route_colour': row[6],
                    'route_text_colour': row[7]
                }
                Route.objects.update_or_create(route_id=data['route_id'], defaults=data)

            case 'shapes.txt':
                data = {
                    'shape_id': row[0],
                    'shape_pt_lat': row[1],
                    'shape_pt_lon': row[2],
                    'shape_pt_sequence': row[3],
                    'shape_dist_traveled': row[4],
                }
                Shape.objects.update_or_create(shape_id=data['shape_id'], defaults=data)

            case 'stop_times.txt':
                data = {
                    'trip_id': row[0],
                    'arrival_time': row[1],
                    'departure_time': row[2],
                    'stop_id': row[3],
                    'stop_sequence': row[4],
                    'stop_headsign': row[5],
                    'pickup_type': row[6],
                    'drop_off_type': row[7],
                    'shape_distance_traveled': row[8],
                    'timepoint': row[9],
                    'stop_note_id': row[10],
                }
                StopTime.objects.update_or_create(trip_id=data['trip_id'], stop_id=data['stop_id'], defaults=data)

            case 'stops.txt':
                data = {
                    'stop_id': row[0],
                    'stop_name': row[2],
                    'stop_lat': row[4],
                    'stop_lon': row[5],
                    'location_type': row[8],
                    'parent_station': row[9],
                    'wheelchair_boarding': row[11],
                    'platform_code': row[12],
                }
                Stop.objects.update_or_create(stop_id=data['stop_id'], defaults=data)

            case 'trips.txt':
                data = {
                    'route_id': row[0],
                    'service_id': row[1],
                    'trip_id': row[2],
                    'trip_headsign': row[3],
                    'direction_id': row[5],
                    'block_id': row[6],
                    'shape_id': row[7],
                    'wheelchair_accessible': row[8],
                    'trip_note_id': row[10],
                    'route_direction': row[11],
                }
                Trip.objects.update_or_create(trip_id=data['trip_id'], defaults=data)

            case 'notes.txt':
                data = {
                    'note_id': row[0],
                    'note_text': row[1],
                }
                Note.objects.update_or_create(note_id=data['note_id'], defaults=data)
                
            case _:
                return
    except Exception as e:
        raise Exception(str(e))
