# Start/Stop EC2 with AWS Lambda

Use two AWS Lambda functions to start/stop EC2 instances based on tags.

# Instructions

1. Use "lambda_policy.json" to provision AWS Lambda with the appropriate permissions to start/stop EC2 instances.
2. Create a "StartEC2" AWS Lambda function which utilizes "startEC2.py" to start instances.
3. Create a "StopEC2" AWS Lambda function which utilizes "stopEC2.py" to stop instances.
4. Create a CloudWatch rule to invoke the "StartEC2" AWS Lambda function at your desired start time.
5. Create a CloudWatch rule to invoke the "StopEC2" AWS Lambda function at your desired stop time.
6. Tag instances with AutoStart: True and AutoStop: True to associate them with the AWS Lambda functions.
