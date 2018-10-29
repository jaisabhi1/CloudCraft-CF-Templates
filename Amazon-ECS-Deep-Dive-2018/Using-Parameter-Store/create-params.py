import boto3
import json
from botocore.vendored import requests


def lambda_handler(event, context):

    kms_client = boto3.client('kms')
    ssm_client = boto3.client('ssm')

    res = kms_client.describe_key(KeyId='alias/prod-app1')
    prodApp1Key = res['KeyMetadata']['KeyId']
    print('prod-app1:', prodApp1Key)

    res = kms_client.describe_key(KeyId='alias/license-code')
    licenseCodeKey = res['KeyMetadata']['KeyId']
    print('license-code:', licenseCodeKey)

    response = ssm_client.put_parameter(
        Name='prod.app1.db-pass',
        Description='Production Application 1 DB Password',
        Value='P@ssw0rd1',
        Type='SecureString',
        KeyId=prodApp1Key,
        Overwrite=True,
    )

    print('RESPONSE:n' + json.dumps(response))

    response = ssm_client.put_parameter(
        Name='prod.app2.user-name',
        Description='Production Application 2 Username',
        Value='johnsmith',
        Type='String',
        Overwrite=True,
    )

    print('RESPONSE:n' + json.dumps(response))

    response = ssm_client.put_parameter(
        Name='general.license-code',
        Description='General license code',
        Value='xJee2HesQy0',
        Type='SecureString',
        KeyId=licenseCodeKey,
        Overwrite=True,
    )

    print('RESPONSE:n' + json.dumps(response))

    responseStatus = 'SUCCESS'
    responseData = {}

    if event['RequestType'] == 'Delete':
        sendResponse(event, context, responseStatus, responseData)

    responseData = {'Success': 'Lambda function invoked'}
    sendResponse(event, context, responseStatus, responseData)


def sendResponse(event, context, responseStatus, responseData):
    responseBody = {'Status': responseStatus,
                    'Reason': 'See the details in CloudWatch Log Stream: ' + context.log_stream_name,
                    'PhysicalResourceId': context.log_stream_name,
                    'StackId': event['StackId'],
                    'RequestId': event['RequestId'],
                    'LogicalResourceId': event['LogicalResourceId'],
                    'Data': responseData}
    print('RESPONSE BODY:n' + json.dumps(responseBody))
    try:
        req = requests.put(event['ResponseURL'], data=json.dumps(responseBody))
        if req.status_code != 200:
            print(req.text)
            raise Exception(
                'Recieved non 200 response while sending response to CFN.')
        return
    except requests.exceptions.RequestException as e:
        print(e)
        raise
