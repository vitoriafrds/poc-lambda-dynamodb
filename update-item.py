import boto3
from datetime import date
from boto3.dynamodb.conditions import Key

def update_item(event, context):
    execution_id = event['executionId']
    print('Processamento para atualizar situação da execução: {id}'.format(id=execution_id))

    dynamo_client = boto3.resource('dynamodb')
    table = dynamo_client.Table('monitoramento-geracao-relatorio')
    
    table.update_item(Key={
        'ExecutionId' : execution_id
    },
    UpdateExpression='set #status = :s',
    ExpressionAttributeValues={
        ':s': 'EXECUTED'
    },
    ExpressionAttributeNames={
    "#status": "Status"
  })

    print('Informações alteradas com sucesso.')
