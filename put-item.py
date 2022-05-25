import json
import boto3
import uuid
from datetime import date

def put_execution_id(event, context):
    execution_id = str(uuid.uuid4())
    print('Iniciando execução de id: {id}'.format(id=execution_id))

    dynamo_client = boto3.resource('dynamodb')
    table = dynamo_client.Table('monitoramento-geracao-relatorio')
    
    table.put_item(Item={
        'ExecutionId' : execution_id,
        'Status' : 'PENDING'
    })

    print('Informações salvas com sucesso.')