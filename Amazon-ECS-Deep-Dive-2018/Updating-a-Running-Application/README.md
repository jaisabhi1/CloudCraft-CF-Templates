# Updating a Running Applicaiton

[CloudCraft](https://cloudcraft.linuxacademy.com/#/labs/details/3d885474-c43c-41ba-a74b-3a8a8ea2bfd1?courseId=261)

In this hands-on learning activity, the student will update a running ECS-deployed application without downtime. You can change the task definition, platform version, deployment configuration, or number of desired tasks (or any combination of these). The goal is to ensure the web application continues to respond uninterrupted during the update.

## Task 1

### To update a running service

1. Open the Amazon ECS console at [https://console\.aws\.amazon\.com/ecs/](https://console.aws.amazon.com/ecs/)\.

1. In the navigation pane, choose **Clusters**\.

1. On the **Clusters** page, select the name of the cluster in which your service resides\.

1. On the **Cluster: *name*** page, choose **Services**\.

1. Check the box to the left of the service to update and choose **Update**\.

1. On the **Configure service** page, your service information is pre\-populated\. Change the task definition, platform version, deployment configuration, or number of desired tasks \(or any combination of these\) and choose **Next step**\.

**Note**
If you want your service to use a newly updated Docker image with the same tag as what is in the existing task definition \(for example, `my_image:latest`\), or keep the current settings for your service, select **Force new deployment**\. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start\. The **Force new deployment** option is also used when updating a Fargate task to use a more current platform version when you specify `LATEST`\. For example, if you specified `LATEST` and your running tasks are using the `1.0.0` platform version and you want them to relaunch using a newer platform version\.

1. On the **Configure network** page, your network information is pre\-populated\. Change the health check grace period \(if desired\) and choose **Next step**\.

1. \(Optional\) You can use Service Auto Scaling to scale your service up and down automatically in response to CloudWatch alarms\.

   1. Under **Optional configurations**, choose **Configure Service Auto Scaling**\.

   1. Proceed to [\(Optional\) Configuring Your Service to Use Service Auto Scaling](create-service.md#service-configure-auto-scaling)\.

   1. Complete the steps in that section and then return here\.

1. Choose **Update Service** to finish and update your service\.
