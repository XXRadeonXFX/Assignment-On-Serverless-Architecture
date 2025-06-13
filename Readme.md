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

## Objective

Automatically delete files older than 30 days in a specific S3 bucket using AWS Lambda and Boto3.

## Steps Followed

1. Created S3 bucket `radeon-s3-cleanup-assignment`.
   ![s3](Screenshots/Screenshot-2-S3-Cleanup/s3.png)

2. Uploaded test files (some new, some old).
   ![upload-files](Screenshots/Screenshot-2-S3-Cleanup/upload-files.png)

3. Create an IAM role `prince-lamda-role-task-1` with `AmazonS3FullAccess`.
   ![IAM-role](Screenshots/Screenshot-2-S3-Cleanup/IAM-role.png)

4. Create Lambda function (in this case its) `prince-lambda` with Python 3.13.
   ![lambda-function](Screenshots/Screenshot-2-S3-Cleanup/lambda-function.png)

5. Lambda function:
    - Lists objects in the bucket.
    - Deletes objects older than 30 days.
    - Logs deleted object names.
   ![python-boto-3-code](Screenshots/Screenshot-2-S3-Cleanup/python-boto-3-code.png)


6. Tested Lambda manually.

## Screenshots

- [ ] S3 bucket and objects
- [ ] IAM Role created
- [ ] Lambda function code + test result
- [ ] S3 bucket after cleanup