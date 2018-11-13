# Deploying an Application to EKS

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/8f76c820-9145-4e84-8113-6bb7a623daef?courseId=293>

Note the `NodeInstanceRole` ARN output value and Cluster Name.

## Kubernetes + CloudFormation issues

CloudFormation can't interact with a K8s cluster in any way. So, after the stack
is up, the student will still have some configuration to do:

1. Install `kubectl`
1. Install `aws-iam-authenticator`
1. Update kube config with the cluster name
1. Join worker nodes to the cluster
1. Deploy the K8s dashboard

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

Edit `aws-auth-cm.yaml` in this directory. Set `rolearn` to the `NodeInstanceRole` ARN value from `nodes.yaml` stack output above.

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

`aws-iam-authenticator token -i <cluster_name> --token-only`

Set this token in the K8s dashboard.