from rest_framework.response import Response
from rest_framework.decorators import api_view
from zipfile import ZipFile
import csv
from io import TextIOWrapper
from . import utils

@api_view(['POST'])
def upload_GTFS_file(request, filename):
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
    
    
