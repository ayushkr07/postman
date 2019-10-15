from django.http import JsonResponse, HttpResponse
import boto3
from postman.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from boto3.session import Session


def upload_to_s3(request):
    if request.method == 'POST':
        uploaded_file= request.FILES['documents']
        session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_S3_REGION_NAME)
        s3 = session.resource('s3')
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=uploaded_file.name,Body=uploaded_file)
    return JsonResponse({'status': 'success', 'message': 'file has been uploaded'}, safe=False)

