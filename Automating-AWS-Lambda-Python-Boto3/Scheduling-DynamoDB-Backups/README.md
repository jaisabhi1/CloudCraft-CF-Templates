# Scheduling DynamoDB Backups

<https://cloudcraft.linuxacademy.com/#/labs/details/36f2b226-5a94-4e3e-8243-4c4474003cba?courseId=313>

The CloudFormation stack creates the following resources:

- DynamoDB table `PersonTable` as the example table to back up.

## Description

Let's assume you want to take a backup of one of your DynamoDB tables each day. We also want to retain backups for a specified period of time. 

A simple way to achieve this is to use an Amazon CloudWatch Events rule to trigger an AWS Lambda function daily. In this hands-on AWS lab, you will write a Lambda function in Python using the Boto3 library.

Setting this up requires configuring an IAM role, setting a CloudWatch rule, and creating a Lambda function.

## Instructions

Make sure you are in the `us-east-1` region.

## Video Description(s)

### Lab Walkthrough

In this video, we'll walk through the process of authoring our IAM Role for the Lambda function, creating the Lambda function itself, and then testing the Lambda function. Once the Lambda function is created, we will create a CloudWatch Rule to schedule the Lambda function to run at regular intervals. This will perform backups of the DynamoDB table, and remove stale backups.

## Tasks

### Task 1 - Create Lambda Function

- Navigate to AWS Lambda
- Create Function
- Author from scratch
- Name: `BackupDynamoDBTable`
- Runtime: `Python 3.7`
- Role: Create a custom role
  - View policy document
  - Edit
  - Paste in the policy from [this file](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Scheduling-DynamoDB-Backups/lambda_execution_role.json) on Github
- Paste Python source code from [this file](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Scheduling-DynamoDB-Backups/lambda_function.py) on Github
- Save the Lambda function

### Task 2 - Configure Test Event

1. On the **Configure test event** page, type an event name, and set the content to `{"TableName": "Person"}`, and choose **Create**.
2. Choose **Test**. It should show a successful execution result.
3. Open the DynamoDB console, and choose **Backups**. The **Backups** page shows you the backup that you took using the Lambda function.

### Task 3 - Create CloudWatch Rule to Trigger Lambda Backup Function

1. Schedule event to run at the desired interval (i.e. every 1 minute), triggering the Lambda function.
2. Set the event value to a constant: `{"TableName": "Person"}`
3. Wait for the CloudWatch rule to trigger the next backup job that you have scheduled.
4. Verify the scheduled backup job ran using CloudWatch Logs.
5. Verify the backup file exists in the list of DynamoDB backups.

<details>
<summary>
Example `BackupSummaries` data
</summary>
<p>

```python
[{
    'TableName': 'Person',
    'TableId': '83a29d55-de0d-4c8b-868a-7a7073504701',
    'TableArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person',
    'BackupArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person/backup/01547836861284-b259a36e',
    'BackupName': 'Person-20190118134101',
    'BackupCreationDateTime': datetime.datetime(2019, 1, 18, 13, 41, 1, 284000, tzinfo=tzlocal()),
    'BackupStatus': 'AVAILABLE',
    'BackupType': 'USER',
    'BackupSizeBytes': 92
}, {
    'TableName': 'Person',
    'TableId': '83a29d55-de0d-4c8b-868a-7a7073504701',
    'TableArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person',
    'BackupArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person/backup/01547836868574-f62a4554',
    'BackupName': 'Person-20190118134108',
    'BackupCreationDateTime': datetime.datetime(2019, 1, 18, 13, 41, 8, 574000, tzinfo=tzlocal()),
    'BackupStatus': 'AVAILABLE',
    'BackupType': 'USER',
    'BackupSizeBytes': 92
}, {
    'TableName': 'Person',
    'TableId': '83a29d55-de0d-4c8b-868a-7a7073504701',
    'TableArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person',
    'BackupArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person/backup/01547836870158-00c5d1bc',
    'BackupName': 'Person-20190118134109',
    'BackupCreationDateTime': datetime.datetime(2019, 1, 18, 13, 41, 10, 158000, tzinfo=tzlocal()),
    'BackupStatus': 'AVAILABLE',
    'BackupType': 'USER',
    'BackupSizeBytes': 92
}, {
    'TableName': 'Person',
    'TableId': '83a29d55-de0d-4c8b-868a-7a7073504701',
    'TableArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person',
    'BackupArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person/backup/01547836871112-ddc91ac4',
    'BackupName': 'Person-20190118134110',
    'BackupCreationDateTime': datetime.datetime(2019, 1, 18, 13, 41, 11, 112000, tzinfo=tzlocal()),
    'BackupStatus': 'AVAILABLE',
    'BackupType': 'USER',
    'BackupSizeBytes': 92
}, {
    'TableName': 'Person',
    'TableId': '83a29d55-de0d-4c8b-868a-7a7073504701',
    'TableArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person',
    'BackupArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person/backup/01547836872046-80b51070',
    'BackupName': 'Person-20190118134111',
    'BackupCreationDateTime': datetime.datetime(2019, 1, 18, 13, 41, 12, 46000, tzinfo=tzlocal()),
    'BackupStatus': 'AVAILABLE',
    'BackupType': 'USER',
    'BackupSizeBytes': 92
}, {
    'TableName': 'Person',
    'TableId': '83a29d55-de0d-4c8b-868a-7a7073504701',
    'TableArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person',
    'BackupArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/Person/backup/01547836872948-da6f16c2',
    'BackupName': 'Person-20190118134112',
    'BackupCreationDateTime': datetime.datetime(2019, 1, 18, 13, 41, 12, 948000, tzinfo=tzlocal()),
    'BackupStatus': 'AVAILABLE',
    'BackupType': 'USER',
    'BackupSizeBytes': 92
}]
```
</details>