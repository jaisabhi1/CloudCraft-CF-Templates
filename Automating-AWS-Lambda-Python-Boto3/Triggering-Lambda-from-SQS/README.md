# Triggering Lambda from SQS

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/6a9d4633-3c46-4086-8451-e92e7c590e4f?courseId=313>

The CloudFormation stack creates the following resources:

- VPC with a public EC2 instance
- SQS queue
- DynamoDB table

## Description

In this hands-on AWS lab, we'll learn how to 

- Download the Lambda execution role IAM policy [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/lambda_execution_role.json)
- Download the Lambda function source code [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/lambda_handler.py)

## Instructions

Make sure you are in the `us-east-1` region.

An SQS topic and DynamoDB table are provided for you.

1. TODO
1. TODO

## Video Description(s)

### Part 1 - Create Elastic Transcoder Pipeline

Pipelines are queues that manage your transcoding jobs. While creating jobs you can specify the settings regarding the location of the input/output file. Presets are templates that specify most of the settings for the transcoded media file.

### Part 2 - Create Lambda Execution Role

Create the Lambda execution role using the IAM policy [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/lambda_execution_role.json)

### Part 3 - Create Lambda Function

Create the Lambda function using the source code [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/lambda_handler.py)

### Part 4 - Upload Video for Transcoding

Download sample 4K videos [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/Aerial.mp4) and [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/Clouds.mp4)

Upload one of the videos to the S3 "source" bucket. Observe that the transcoded videos appear in the "transcoded" bucket.

## Tasks

### Task 1 - Subscribe to SNS Topic

- In the AWS Management Console, navigate to SNS.
- Select the "Transcode" topic.
- Under "Actions", select "Subscribe to topic"
- In the Protocol drop-down box, select Email.
- In the Endpoint box, type an email address you can use to receive the notification.
- Choose Create subscription.
- Go to your email application and open the message from AWS Notifications, and then choose the link to confirm your subscription.

### Task 2 - Create Elastic Transcoder Pipeline

- In the AWS Management Console, navigate to Elastic Transcoder
- Under Pipelines, select "Create New Pipeline"
- Pipeline Name: Enter any name you like
- Input bucket: Select the existing bucket with `source` in the name
- Allow the IAM role to be created automatically
- For transcoded files, select the existing bucket with `transcoded` in the name
- Storage Class: Choose either Standard or Reduced Redundancy
- For thumbnails, select the existing bucket with `thumbnails` in the name
- Storage Class: Choose either Standard or Reduced Redundancy
- Note the Pipeline ID. This is available under pipeline details, and is a *different* value than the pipeline name.

### Task 3 - Create Lambda Function

- In the AWS Management Console, navigate to AWS Lambda
- Select Create Function
- Give the function any name you like
- For runtime, choose `Python 3.7`
- Create a custom role, using the IAM policy [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/lambda_execution_role.json)
- Select create function
- Select S3 as the trigger, and choose the bucket with `source` in the name
- Select "All object create events"
- Click "Add"
- Click the function name at the top of the page to enable the function editor
- Paste in the function body using the source code [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/lambda_handler.py)
- Set an environment variable called `PIPELINE_ID` and set its value to the pipeline ID from the previous task.
- Save the Lambda function

### Task 4 - Upload Video for Transcoding

- Download the sample 4K videos [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/Aerial.mp4) and [here](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Video-Transcoding/Clouds.mp4)
- Navigate to the S3 bucket with `source` in its name.
- Upload one of the 4K video files.
- Observe in CloudWatch Logs and in your email inbox that the transcoding job completed successfully.
- Navigate to the S3 bucket with `transcoded` in its name.
- Verify that 1080p and 720p versions of your uploaded video are present.

<details>
<summary>
Example S3 Event
</summary>
<p>

```json
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "<bucketname>",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::<bucketname>"
        },
        "object": {
          "key": "Street-3840×2160.mp4",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}

```
</details>