# Daily-Gym-Motivation-Scheduler

I built a scheduler to send me gym motivation videos daily at 4pm (just before my evening workout).

## Technologies used

AWS Lambda to run Python script
AWS Simple Notification Service (SNS)
AWS EventBridge to schedule the job
Google Cloud Platform to generate YouTube API key and monitor usage

## How to Setup

1. Create a new Function in AWS Lambda with runtime Python 3.8 or later
2. Copy the code in lambda_function.py and paste it in your lambda function
3. Create a new Topic in AWS SNS and not it's ARN
4. Create a new Subscription and enter your email/phone number where you want to receive the notification
5. Navigate to "Schedules" in AWS EventBridges, and create a new Schedule.
   a. Set Occurence as Recurring & Schedule Type as Cron-based
   b. Enter the time you want to run the job daily as a Cron expression. For eg. 4pm is "0 16 * * ? *"
   c. Enter "Target" as your Lambda Function


## Use Cases

This simple scheduler can be used for a multitude of purposes like 
-> cold emailing while applying for jobs
-> daily reminders for mundane tasks
-> Weather alerts
-> Stock market fluctuations
-> Meeting reminders
