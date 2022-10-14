from rest_framework.response import Response
from rest_framework.decorators import api_view
from zipfile import ZipFile
import csv
from io import TextIOWrapper


def get_filenames(path_to_zip):
    """ return list of filenames inside of the zip folder"""
    with ZipFile(path_to_zip, 'r') as zip:
        return zip.namelist()


@api_view(['POST'])
def upload_GTFS_file(request, filename):
    file_obj = request.data['file']

    try:
        filenames = get_filenames(file_obj)
    except:
        return Response(data={'message': 'Invalid file format'}, status=415)

    required_filenames = ['agency.txt', 'calendar.txt', 'calendar_dates.txt',
                          'notes.txt', 'routes.txt', 'shapes.txt', 'stop_times.txt', 'stops.txt', 'trips.txt']
    is_valid_filenames = all(item in filenames for item in required_filenames)

    if not is_valid_filenames:
        return Response(data={'message': 'Invalid GTFS zip file'}, status=415)

    with ZipFile(file_obj, 'r') as zip:
        for csv_name in zip.namelist():
            with zip.open(csv_name, 'r') as file:
                reader = csv.reader(TextIOWrapper(file, 'utf-8'))
                next(reader, None)  # to skip header
                for row in reader:
                    # Todo: process the CSV logic here
                    print(row)
            break  # To be removed

    return Response(data={'message': 'Process file successfully!'}, status=201)
