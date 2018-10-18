# Sending SNS Alerts for ECS Events

[CloudCraft](https://cloudcraft.linuxacademy.com/#/labs/details/1087ff69-a9e7-4a12-8915-aa9fc73fc84e?courseId=261)

In this hands-on learning activity, the student will learn how to configure SNS Alerts for ECS Events. These events can be sent to the student's email address, or be used to trigger Lambda functions.

## Task 1: Create and Subscribe to an Amazon SNS Topic

 For this tutorial, you configure an Amazon SNS topic to serve as an event target for your new event rule\.

### To create a Amazon SNS topic

1. Open the Amazon SNS console at [https://console\.aws\.amazon\.com/sns/v2/home](https://console.aws.amazon.com/sns/v2/home)\.

1. Choose **Topics**, **Create new topic**\.

1. On the **Create new topic** window, for **Topic name**, enter **TaskStoppedAlert** and choose **Create topic**\.

1. On the **Topics** window, select the topic that you just created\. On the **Topic details: TaskStoppedAlert** screen, choose **Create subscription**\.

1. On the **Create Subscription** window, for **Protocol**, choose **Email**\. For **Endpoint**, enter an email address to which you currently have access and choose **Create subscription**\.

1. Check your email account, and wait to receive a subscription confirmation email message\. When you receive it, choose **Confirm subscription**\.

## Task 2: Register Event Rule

 Next, you register an event rule that captures only task\-stopped events for tasks with stopped containers\.

### To create an event rule

1. Open the CloudWatch console at [https://console\.aws\.amazon\.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)\.

1. On the navigation pane, choose **Events**, **Create rule**\.

1. Choose **Show advanced options**, **edit**\.

1. For **Build a pattern that selects events for processing by your targets**, replace the existing text with the following text:

   ```JSON
   {
   "source": [
     "aws.ecs"
   ],
   "detail-type": [
     "ECS Task State Change"
   ],
   "detail": {
     "lastStatus": [
       "STOPPED"
     ],
     "stoppedReason" : [
       "Essential container in task exited"
     ]
   }
   }
   ```

   This code defines a CloudWatch Events event rule that matches any event where the `lastStatus` and `stoppedReason` fields match the indicated values\. For more information about event patterns, see [Events and Event Patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html) in the *Amazon CloudWatch User Guide*\.

1. For **Targets**, choose **Add target**\. For **Target type**, choose **SNS topic**, and then choose **TaskStoppedAlert**\.

1. Choose **Configure details**\.

1. For **Rule definition**, type a name and description for your rule and then choose **Create rule**\.

## Task 3: Test Your Rule

 To test your rule, you attempt to run a task that exits shortly after it starts\. If your event rule is configured correctly, you receive an email message within a few minutes with the event text\.

### To test a rule

1. Open the Amazon ECS console at [https://console\.aws\.amazon\.com/ecs/](https://console.aws.amazon.com/ecs/)\.

1. Choose **Task Definitions**, **Create new Task Definition**\.

1. For **Task Definition Name**, type **WordPressFailure** and choose **Add Container**\.

1. For **Container name**, type **Wordpress**, for **Image**, type **wordpress**, and for **Maximum memory \(MB\)**, type **128**\.

1. Choose **Add**, **Create**\.

1. On the **Task Definition** screen, choose **Actions**, **Run Task**\.

1. For **Cluster**, choose **default** and then **Run Task**\.

1. On the **Tasks** tab for your cluster, periodically choose the refresh icon until you no longer see your task running\. For **Desired task status**, choose **Stopped** to verify that your task has stopped\.

1. Check your email to confirm that you have received an email alert for the stopped notification\.