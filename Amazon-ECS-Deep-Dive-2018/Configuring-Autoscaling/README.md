# Configuring Autoscaling

CloudCraft: <https://cloudcraft.linuxacademy.com/#/labs/details/5a14c9c6-39fb-4f6d-9351-ed119c22e3c7?courseId=261>

AWS: [Target Tracking Scaling Policies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-autoscaling-targettracking.html)

## Step 1: Configure Service Auto Scaling

Now that you have launched a cluster and created a service in that cluster that is running behind a load balancer, you can configure Service Auto Scaling by creating scaling policies to scale your service out and in in response to CloudWatch alarms\.

### To configure basic Service Auto Scaling parameters

1. On the **Service: webapp** page, your service configuration should look similar to the image below \(although the task definition revision and load balancer name will likely be different\)\. Choose **Update** to update your new service\.
![\[Choose your configuration options\]](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/images/sample-app-service.png)

1. On the **Update service** page, choose **Next step** until you get to **Set Auto Scaling \(optional\)**\.

1. For **Service Auto Scaling**, choose **Configure Service Auto Scaling to adjust your service’s desired count**\.

1. For **Minimum number of tasks**, enter `1` for the lower limit of the number of tasks for Service Auto Scaling to use\. Your service's desired count is not automatically adjusted below this amount\.

1. For **Desired number of tasks**, this field is pre\-populated with the value that you entered earlier\. This value must be between the minimum and maximum number of tasks specified on this page\. Leave this value at `1`\.

1. For **Maximum number of tasks**, enter `2` for the upper limit of the number of tasks for Service Auto Scaling to use\. Your service's desired count is not automatically adjusted above this amount\.

1. For **IAM role for Service Auto Scaling**, choose an IAM role to authorize the Application Auto Scaling service to adjust your service's desired count on your behalf\. If you have not previously created such a role, choose **Create new role** and the role is created for you\. For future reference, the role that is created for you is called `ecsAutoscaleRole`\. For more information, see [Amazon ECS Service Auto Scaling IAM Role](autoscale_IAM_role.md)\.

### To configure scaling policies for your service

These steps help you create scaling policies and CloudWatch alarms that can be used to trigger scaling activities for your service\. You can create a scale\-out alarm to increase the desired count of your service, and a scale in alarm to decrease the desired count of your service\.

1. Choose **Add scaling policy** to configure your scaling policy\.

1. On the **Add policy** page, do the following:

   1. For **Scaling policy type**, choose **Target tracking**\.

   1. For **Policy name**, enter `TargetTrackingPolicy`\.

   1. For **ECS service metric**, choose **CPUUtilization**\.

   1. For **Target value**, enter `75`\.

   1. For **Scale\-out cooldown period**, enter `60`\. This is the amount of time, in seconds, after a scale\-out activity completes before another scale\-out activity can start\. During this time, resources that have been launched do not contribute to the Auto Scaling group metrics\.

   1. For **Scale\-in cooldown period**, enter `60`\. This is the amount of time, in seconds, after a scale in activity completes before another scale in activity can start\. During this time, resources that have been launched do not contribute to the Auto Scaling group metrics\.

   1. Choose **Save**\.

1. Choose **Next step**\.

1. Review all of your choices and then choose **Update Service**\.

1. When your service status is finished updating, choose **View Service**\.

## Step 2: Trigger a Scaling Activity

After your service is configured with Service Auto Scaling, you can trigger a scaling activity by pushing your service's CPU utilization into the `ALARM` state\. Because the example in this tutorial is a web application that is running behind a load balancer, you can send thousands of HTTP requests to your service \(using the ApacheBench utility\) to spike the service CPU utilization above the threshold amount\. This spike should trigger the alarm, which in turn triggers a scaling activity to add one task to your service\.

After the ApacheBench utility finishes the requests, the service CPU utilization should drop below your 25% threshold, triggering a scale in activity that returns the service's desired count to 1\.

### To trigger a scaling activity for your service

1. From your service's main view page in the console, choose the load balancer name to view its details in the Amazon EC2 console\. You need the load balancer's DNS name, which should look something like `http://YOUR_ALB_ENDPOINT_HERE.us-east-1.elb.amazonaws.com`\.

1. Use the ApacheBench \(ab\) utility to make thousands of HTTP requests to your load balancer in a short period of time\.

**Note**
This command is installed by default on macOS, and it is available for many Linux distributions, as well\. For example, you can install ab on Amazon Linux with the following command:

   ```bash
   $ sudo yum install -y httpd24-tools
   ```

   Run the following command, substituting your load balancer's DNS name\.

   ```bash
   $ ab -n 1000000 -c 2000 http://http://YOUR_ALB_ENDPOINT_HERE.us-east-1.elb.amazonaws.com/
   ```

1. Open the CloudWatch console at [https://console\.aws\.amazon\.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)\.

1. In the left navigation pane, choose **Alarms**\.

1. Wait for your ab HTTP requests to trigger the scale\-out alarm in the CloudWatch console\. You should see your Amazon ECS service scale out and add 1 task to your service's desired count\.

1. Shortly after your ab HTTP requests complete \(between 1 and 2 minutes\), your scale in alarm should trigger and the scale in policy reduces your service's desired count back to 1\.
