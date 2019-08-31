import boto3
import json
import requests

BUCKET = 'rhombuscandidate'

address = 'http://0.0.0.0:4848' 
URL = address + '/predict'

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)

for obj in bucket.objects.filter(Prefix = 'Input') :
    if obj.key != "Input/" :
      key = str(obj.key)
      headers = {'file': key}
      body = obj.get()['Body'].read().decode('utf-8')
      s3.Bucket(BUCKET).download_file(key, 'temp.json')
      with open('temp.json') as json_file :
        json_data = json.load(json_file)
      res = requests.post(URL, json = json_data, headers = headers)
      print(res)
      

print("Finished sending requests")

