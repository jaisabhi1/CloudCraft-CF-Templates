# Configuring Autoscaling

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/5a14c9c6-39fb-4f6d-9351-ed119c22e3c7?courseId=261>

## To generate load with Apache Bench

`while true; do ab -n 500000 -c 1000 http://YOUR_ALB_ENDPOINT_HERE.us-east-1.elb.amazonaws.com/ ; done`
