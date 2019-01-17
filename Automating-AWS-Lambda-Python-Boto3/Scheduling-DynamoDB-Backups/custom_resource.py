import boto3
import cfnresponse


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table("Person")
        table.put_item(
            Item={'id': 1, 'last_name': 'Doe', 'first_name': 'John'})
        table.put_item(
            Item={'id': 2, 'last_name': 'Doe', 'first_name': 'Jane'})
        table.put_item(
            Item={'id': 3, 'last_name': 'Bloggs', 'first_name': 'Joe'})
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    except Exception:
        cfnresponse.send(event, context, cfnresponse.FAILED, {})
