# Creating an EKS Cluster

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/ac1a30ba-63c7-497f-85c9-41e8087e903e?courseId=293>

This template only creates API keys for `cloud_user`. The student is expected to run the AWS-supplied CloudFormation templates themselves in order to create the cluster and worker nodegroup.

## Create the EKS Service Role

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. Choose **Roles**, then **Create role**\.

1. Choose **EKS** from the list of services, then **Allows Amazon EKS to manage your clusters on your behalf** for your use case, then **Next: Permissions**\.

1. Choose **Next: Review**\.

1. For **Role name**, enter a unique name for your role, such as `eksServiceRole`, then choose **Create role**\.

## Create the EKS Cluster VPC

Run this CloudFormation template: <https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-11-07/amazon-eks-vpc-sample.yaml>

## Create Key Pair

1. Open the Amazon EC2 console at [https://console\.aws\.amazon\.com/ec2/](https://console.aws.amazon.com/ec2/)\.

1. In the navigation pane, under **NETWORK & SECURITY**, choose **Key Pairs**.

1. Choose **Create Key Pair**.

1. Enter a name for the new key pair in the **Key pair name** field of the **Create Key Pair** dialog box, and then choose **Create**.

1. The private key file (`.pem`) is automatically downloaded by your browser.

## Create the EKS Worker Node Group

Run this CloudFormation template:
<https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-11-07/amazon-eks-nodegroup.yaml>

Record the `NodeInstanceRole` ARN for the node group that was created. You will need this when you configure your EKS worker nodes in a later step.

## Install kubectl

Full instructions here: <https://docs.aws.amazon.com/eks/latest/userguide/configure-kubectl.html>

For example, to install version 1.10.3 on macOS:

```sh
curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/darwin/amd64/kubectl

chmod +x ./kubectl
```

Ensure that `kubectl` is in your `PATH`.

## Install aws-iam-authenticator

For example, to install version 1.10.3 for macOS:

```sh
curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/darwin/amd64/aws-iam-authenticator

chmod +x ./aws-iam-authenticator
```

Ensure that `aws-iam-authenticator` is in your `PATH`.

## Configure kubeconfig file

`aws eks update-kubeconfig --name <cluster name>`

## Enable worker Nodes to Join Cluster

Edit `aws-auth-cm.yaml` in this directory. Set `rolearn` to the `NodeInstanceRole` ARN value from the worker node group CloudFormation stack output you ran previously.

Apply the configuration:

`kubectl apply -f aws-auth-cm.yaml`

Watch the nodes join the cluster:

`kubectl get nodes --watch`

## Deploy the Kubernetes Dashboard

Full instructions here: <https://docs.aws.amazon.com/eks/latest/userguide/dashboard-tutorial.html>

`kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml`

`kubectl proxy &`

Open <http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/>

## Get an authentication token

`aws-iam-authenticator token -i <cluster_name>`

Set this token in the K8s dashboard.