import boto3
import uuid
import json
from boto3.dynamodb.conditions import Key

def put_execution_id(event, context):
    execution_id = event['executionId']
    print('Iniciando consulta da execução de id: {id}'.format(id=execution_id))

    dynamo_client = boto3.resource('dynamodb')
    table = dynamo_client.Table('monitoramento-geracao-relatorio')
    
    response = table.get_item(Key={
        'ExecutionId' : execution_id
    })

    print(json.dumps(response))