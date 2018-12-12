# Deploying an Application to EKS

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/8f76c820-9145-4e84-8113-6bb7a623daef?courseId=293>

```bash
kubectl create deployment --image nginx nginx
kubectl get pods
kubectl expose deployment nginx --port=80 --type=LoadBalancer
kubectl get services -o wide
aws elb describe-instance-health --load-balancer-name <name of ELB>
```