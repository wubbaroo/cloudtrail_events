import boto3
import json
import datetime

def datetime_2_string(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

response = boto3.client(service_name='cloudtrail',region_name='<CHANGE-ME-region>',aws_access_key_id='CHANGE-ME-access_key',aws_secret_access_key='CHANGE-ME-secret_key').lookup_events()

events_dumps = json.dumps(response['Events'], default = datetime_2_string)


events_list = json.JSONDecoder().decode(events_dumps)

with open('events.json', 'w') as jfile:
    for e in events_list:
        jfile.write(str(e)+'\n')
