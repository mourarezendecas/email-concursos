import json
from main_orchestrator import execute

def lambda_handler(event, context):
    execute()
    return {
        'statusCode': 200,
        'body': json.dumps('Emails sent!')
    }