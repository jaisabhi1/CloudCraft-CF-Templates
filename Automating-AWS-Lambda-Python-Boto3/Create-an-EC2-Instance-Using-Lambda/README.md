# Create an EC2 Instance Using Lambda

## Create EC2 Keypair

Save keypair locally and set perms:

```sh
chmod 400 keypair.pem
```

## Create Lambda Function

Name: `CreateEC2Instance`

Runtime: `Python 3.7`

Role: `Create new`

### Create Lambda Execution Role

Add statement to policy:

```json
{
  "Action": [
    "ec2:RunInstances"
  ],
  "Effect": "Allow",
  "Resource": "*"
}
```

### Write Function Body

## Set Environment Variables

`AMI`,`INSTANCE_TYPE`,`KEY_NAME`,`SUBNET_ID`

## Test Function

Note output for `instance id`

## Connect to EC2 instance

```sh
ssh -i keypair.pem ec2-user@<ip address>
```