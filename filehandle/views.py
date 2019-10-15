from django.shortcuts import render
#from django.core.files.storage import FileSystemStorage

import boto3
from postman.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from boto3.session import Session

"""def index(request):
    if request.method =='POST':
        uploaded_file= request.FILES['documents']
        fs =FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'base.html')"""

def index(request):
    if request.method =='POST':
        uploaded_file= request.FILES['documents']
        session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_S3_REGION_NAME)
        s3 = session.resource('s3')
        context={'name':uploaded_file.name}
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=uploaded_file.name,Body=uploaded_file)
            #return render(request, 'success.html',context)
    return render(request,'base.html')

