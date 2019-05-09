import json
import boto3
from botocore.vendored import requests
import os

def lambda_handler(event, context):
    # TODO implement
    # process S3 upload event
    print(event)
    bucketname = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    created_time = event['Records'][0]['eventTime']
    file_url = "https://s3.amazonaws.com/"+bucketname+"/"+filename
    print(file_url, created_time)
    # detect labels in images using rekognition
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucketname,
                'Name': filename,
            }
        },
        MaxLabels=15,
        MinConfidence=0.7
    )
    print(response)
    labels = []
    for l in response['Labels']:
        labels.append(l['Name'].lower())
    print(labels)
    # upload json object to ElasticSearch
    #host = 'https://search-photos-wfpwszyhoctjdiqkddxwfwfz6y.us-east-1.es.amazonaws.com'
    host = 'https://vpc-smart-photo-es-2-z22hwml5h2cncxmpf3mfkrzoy4.us-east-1.es.amazonaws.com'
    index = 'photos'
    type = 'pics'
    url = host + '/' + index + '/' + type
    headers = { "Content-Type": "application/json" }
    document = {'objectKey':filename, 
        'bucket':bucketname, 
        'createdTimestamp':created_time, 
        'labels':labels}
    print(document)
    print(url)
    r = requests.post(url, json=document, headers=headers)
    print("response of ES: "+str(r.json()))
    # return
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda: index-photos!')
    }
