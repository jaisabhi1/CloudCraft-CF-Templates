# Deploying an Application to EKS

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/?courseId=>

Note the `NodeInstanceRole` ARN output value and Cluster Name.

## Kubernetes + CloudFormation issues

CloudFormation can't interact with a K8s cluster in any way. So, after the stack
is up, the student will still have some configuration to do:

1. Update kube config with the cluster name
1. Join worker nodes to the cluster
1. Deploy the K8s dashboard

## Configure kubeconfig file

`aws eks update-kubeconfig --name <cluster name>`

## Enable worker Nodes to Join Cluster

Edit `aws-auth-cm.yaml` in this directory. Set `rolearn` to the `NodeInstanceRole` ARN value from `nodes.yaml` stack output above.

Apply the configuration:

`kubectl apply -f aws-auth-cm.yaml`

Watch the nodes join the cluster:

`kubectl get nodes --watch`

## Deploy the Kubernetes Dashboard

`kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml`

`kubectl proxy &`

Open <http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/>

## Get an authentication token

`aws-iam-authenticator token -i <cluster_name> --token-only`

Set this token in the K8s dashboard.