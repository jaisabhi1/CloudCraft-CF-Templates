# Configuring Autoscaling

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/5a14c9c6-39fb-4f6d-9351-ed119c22e3c7?courseId=261>

## To generate load with Apache Bench

[Target Tracking Scaling Policies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-autoscaling-targettracking.html)

- `ab` is installed by default on macOS.
- To install on Amazon Linux: `sudo yum install -y httpd24-tools`.

Run the following command, substituting your load balancer's DNS name:

`ab -n 100000 -c 1000 http://YOUR_ALB_ENDPOINT_HERE.us-east-1.elb.amazonaws.com/`
