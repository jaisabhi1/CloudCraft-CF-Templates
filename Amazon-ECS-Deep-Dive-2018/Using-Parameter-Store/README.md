# Using Parameter Store

<https://cloudcraft.linuxacademy.com/#/labs/details/a006fa86-ac03-48f8-ab62-b55ca2c19da8?courseId=261>

KMS Keys are already created by the CF stack.

SecureString SSM Parameters can not yet be *created* by CloudFormation.

Lambda function is created and invoked by CloudFormation, which handles the SSM Parameter creation.

## Task 1: Create and Attach IAM Policy to ECS Task IAM Role

<https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-templateexamples>

Use `app1-secret-access.json` as a template.

## Task 2: Run Task

Run the task definition `access-test` created in the previous step.

## Task 3: Verify Access

After the task is in a running state, check the public IP of the container instance and navigate to the following page:

`http://<Container-Instance-Public-IP>/ecs.html`

The commands with access to both the parameters and keys should work. Others will fail with an Access Denied Exception.
