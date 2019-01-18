# Scheduling DynamoDB Backups

<https://cloudcraft.linuxacademy.com/#/labs/details/36f2b226-5a94-4e3e-8243-4c4474003cba?courseId=313>

The CloudFormation stack creates the following resources:

1. DynamoDB table `PersonTable` as the example table to back up.
1. S3 bucket to receive the backups

## Tasks

### Task 1 - Create IAM Role with Permission to Perform DynamoDB Backups

```json
{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Action": [
        "dynamodb:CreateBackup",
        "dynamodb:DeleteBackup",
        "dynamodb:DeleteBackup",
        "dynamodb:ListBackups"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

### Task 2 - Create Lambda Function

1. Create Lambda Function
2. Select IAM role created in the previous task.
3. Select Runtime: `Python 3.7`

Use `lambda_function.py`.

### Task 3 - Configure Test Event

1. On the **Configure test event** page, type an event name, ignore the other settings, and choose **Create**.
1. Choose **Test**. It should show a successful execution result.
1. Open the DynamoDB console, and choose **Backups**. The **Backups** page shows you the backup that you took using the Lambda function.
1. Verify the backup file exists in the S3 bucket.

### Task 4 - Create CloudWatch Rule to Trigger Lambda Backup Function

1. Schedule event to run at the desired interval, triggering the Lambda function.
1. Wait for the CloudWatch rule to trigger the next backup job that you have scheduled.
1. Verify the scheduled backup job ran.
1. Verify the backup file exists in the S3 bucket.