# Text-Narrator-using-AWS-Polly-and-Lambda


This project demonstrates a serverless text-to-speech system built using AWS services. 
The system converts input text into natural-sounding speech and stores the generated audio file in Amazon S3.

AWS Services Used
- AWS Lambda - for function
- Amazon Polly
- Amazon S3 - for storage
- AWS IAM - for security and managment



Architecture
API-less serverless execution using Lambda:
1. Lambda function triggers Amazon Polly
2. Polly converts text into speech
3. Generated MP3 file is stored in S3


Workflow
1. Lambda function is invoked manually
2. Text is sent to Amazon Polly
3. Polly generates MP3 audio
4. Audio file is uploaded to S3 bucket

