# Create an EC2 Instance Using Lambda

In this AWS hands-on lab, you will write a Lambda function which will create an EC2 instance. This Lambda function will be written in Python using the Boto3 library. You will also create a custom Lambda execution policy. When you're done, you will be able to SSH into the new EC2 instance.

## Tasks

### Task 1 - Create EC2 Keypair

1. Open the Amazon EC2 console at [https://console\.aws\.amazon\.com/ec2/](https://console.aws.amazon.com/ec2/)\.

2. In the navigation pane, under **NETWORK & SECURITY**, choose **Key Pairs**\.
**Note**  
The navigation pane is on the left side of the Amazon EC2 console\. If you do not see the pane, it might be minimized; choose the arrow to expand the pane\. 

1. Choose **Create Key Pair**\.

1. Enter a name for the new key pair in the **Key pair name** field of the **Create Key Pair** dialog box, and then choose **Create**\.

1. The private key file is automatically downloaded by your browser\. The base file name is the name you specified as the name of your key pair, and the file name extension is `.pem`\. Save the private key file in a safe place\.
**Important** This is the only chance for you to save the private key file\. You'll need to provide the name of your key pair when you launch an instance and the corresponding private key each time you connect to the instance\.

1. If you will use an SSH client on a Mac or Linux computer to connect to your Linux instance, use the following command to set the permissions of your private key file so that only you can read it\.

   ```sh
   chmod 400 my-key-pair.pem
   ```

   If you do not set these permissions, then you cannot connect to your instance using this key pair\.

### Task 2 - Create Lambda Function

- Navigate to AWS Lambda
- Create Function
- Author from scratch
- Name: `CreateEC2Instance`
- Runtime: `Python 3.7`
- Role: Create a custom role
  - View policy document
  - Edit
  - Paste in the policy from [this file](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Lab-Create-an-EC2-Instance-Using-Lambda/lambda_execution_role.json) on Github
- Paste Python source code from [this file](https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Lab-Create-an-EC2-Instance-Using-Lambda/lambda_function.py) on Github
- Set environment variables for `AMI`, `INSTANCE_TYPE`, `KEY_NAME`, `SUBNET_ID`
  - `AMI` can be found under EC2 if you try to launch a new instance. Select `Amazon Linux 2`.
  - `INSTANCE_TYPE` is `t2.micro`
  - `KEY_NAME` is the name of the EC2 keypair you created earlier
  - `SUBNET_ID` is the ID of one of the public subnets in your VPC
- Save the Lambda function

### Task 3 - Test Lambda Function

- Click Test
- Define an empty test event. Its contents can simply be `{}`.
- Give it any name you like.
- Click Create
- Click Test
- Observe that an EC2 instance is initializing

### Task 4 - Connect to the EC2 Instance via SSH

- From the command line, using the `.pem` file you downloaded earlier.
- Connect using the public IP of the EC2 instance.

For example:

`ssh -i mykeypair.pem ec2-user@<IP ADDRESS>`

where `<IP ADDRESS>` is the public IP of the EC2 instance you created.