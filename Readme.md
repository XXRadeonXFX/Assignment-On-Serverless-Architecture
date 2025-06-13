# Assignment 1 - Automated EC2 Instance Management

## Objective

Automatically stop EC2 instances tagged `Auto-Stop` and start instances tagged `Auto-Start` using AWS Lambda and Boto3.

## Steps Followed

1. Create two EC2 instances:
    - One tagged with `Action: Auto-Start`
    ![prince-ec2-start](Screenshots/Screenshot-1-EC2-Auto-Stop-Start/ec2-start.png)



    - One tagged with `Action: Auto-Stop`
    ![prince-ec2-stop](Screenshots/Screenshot-1-EC2-Auto-Stop-Start/ec2-stop.png)

2. Create an IAM role `prince-lamda-role-task-1` with `AmazonEC2FullAccess`.
    ![prince-lamda-role-task-1](Screenshots/Screenshot-1-EC2-Auto-Stop-Start/iam-role.png)

3. Create Lambda function (in this case its) `prince-lambda` with Python 3.13.
    ![prince-lambda](Screenshots/Screenshot-1-EC2-Auto-Stop-Start/lambda-function.png)

4. Lambda function uses Boto3 to:
    - Stop running instances tagged `Auto-Stop`.
    - Start stopped instances tagged `Auto-Start`.
    ![python-boto-3-code](Screenshots/Screenshot-1-EC2-Auto-Stop-Start/python-boto-3-code.png)

5. Manually invoked the Lambda function and verified EC2 instance state changes.
    ![invoke-lambda-function](Screenshots/Screenshot-1-EC2-Auto-Stop-Start/invoke-lambda-function.png)


______________________________________________
# Assignment 2 - Automated EC2 Instance Management
