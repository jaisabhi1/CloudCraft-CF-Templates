# Autoscaling an EKS Cluster

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/b58515c9-c3a9-4a04-b9d7-6a27bb702a05?courseId=293>

## Configure the Cluster Autoscaler

Find autoscaling group for your worker nodes using the AWS Management Console, noting its name.

Edit the ASG's min/max size to 2 and 8 nodes, respectively.

Edit `cluster_autoscaler.yaml`, replacing `<AUTOSCALING GROUP NAME>` with the ASG name you found in the console.

## Create an IAM Policy


## Deploy the Cluster Autoscaler

Deploy the autoscaler:

`kubectl apply -f cluster_autoscaler.yaml`

Watch the logs:

`kubectl logs -f deployment/cluster-autoscaler -n kube-system`

## Scale Out

```bash
kubectl apply -f nginx.yaml
kubectl get deployment/nginx-scaleout
kubectl scale --replicas=10 deployment/nginx-scaleout
kubectl get pods -o wide --watch
```

To view the Cluster Autoscaler logs:

`kubectl logs -f deployment/cluster-autoscaler -n kube-system`

## Cleaning Up

Delete the cluster autoscaler and nginx deployments:

```bash
kubectl delete -f cluster_autoscaler.yaml
kubectl delete -f nginx.yaml
```
