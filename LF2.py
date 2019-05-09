import json
import boto3
from botocore.vendored import requests

def lambda_handler(event, context):
    # get info from input
    print("LOG: Event received from API Gateway is...")
    print(json.dumps(event))
    # print(context)
    # query 
    q = event['q']
    print(q)
    # disambiguate using Lex
    client = boto3.client('lex-runtime')
    response = client.post_text(
        botName='searchphotos',
        botAlias='searchbot',
        userId='10',
        sessionAttributes={
            },
        requestAttributes={
        },
        inputText = q
    )
    print(response)
    keyword_list = []
    try:
        if response['slots']['Query_one']:
            keyword_list.append(response['slots']['Query_one'])
        if response['slots']['Query_two']:
            keyword_list.append(response['slots']['Query_two'])
    except:
        pass
    print(keyword_list)
    if len(keyword_list) > 0:
        keyword = keyword_list[0]
    else:
        keyword = ""
    # Search ES for images  
    searchURL = 'https://vpc-smart-photo-es-2-z22hwml5h2cncxmpf3mfkrzoy4.us-east-1.es.amazonaws.com/photos/_search?q=labels:'
    # searchURL = 'https://vpc-smart-photo-es-2-z22hwml5h2cncxmpf3mfkrzoy4.us-east-1.es.amazonaws.com/photos/_search?q='
    query = '"' + keyword + '"'
    fullURL = searchURL + query 
    print(fullURL)
    #r2 = requests.get('https://vpc-smart-photo-album-es-dvg53fipxeo2fngdqndzm5xsey.us-east-1.es.amazonaws.com/photos/_search?q="Anathem"')
    r2 = requests.get(fullURL)
    print(r2.json())
    
    # return result 
    return {
        'statusCode': 200,
        'body': json.dumps(r2.json())
    }
