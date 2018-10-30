# Using Parameter Store

KMS Keys are already created by the CF stack.

SecureString SSM Parameters can not yet be *created* by CloudFormation.

Lambda function is created and invoked by CloudFormation, which handles the SSM Parameter creation.

## Task 1: Create an ECS Task IAM Role and Policy

<https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-templateexamples>

```bash
AWS_ACCOUNT_ID=<Your_AWS_Account_ID>
aws iam create-role --role-name prod-app1 --assume-role-policy-document file://ecs-tasks-trust-policy.json
aws iam create-policy --policy-name prod-app1 --policy-document file://app1-secret-access.json
aws iam attach-role-policy --role-name prod-app1 --policy-arn "arn:aws:iam::$AWS_ACCOUNT_ID:policy/prod-app1"
```

## Task 2: Upload Test Script to S3

Upload `access-test.sh` to the public S3 bucket automatically generated in your account.

## Task 3: Register Task Definition

Be sure to set values for `ACCOUNT_ID` and `S3_URI` in `create-taskdef.sh` before running this script.

`./create-taskdef.sh` will create a task definition called `access-test`.

## Task 4: Run Task

Run the task definition `access-test` created in the previous step.

## Task 5: Verify Access

After the task is in a running state, check the public IP of the container instance and navigate to the following page:

`http://<Container-Instance-Public-IP>/ecs.html`

Only the first command with the `--no-with-decryption` parameter should work. The policy allows access to the parameter in Parameter Store but there’s no access to the KMS key.

The second command should fail with an access denied error.