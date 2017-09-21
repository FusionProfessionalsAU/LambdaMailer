## Lambda Scheduled s3 CSV bulk Mailer

# Setup

# IAM Role Policies needed

 *SES (You will need to enable ses mail address)
 *LAMBDA
 *S3 (For bucket access)
 
# Create a cloud watch event that triggers the lambda function

parameters

`{
  "bucket": "bucket name",
  "filename": "file",
  "from": "from ses email",
  "body": "mail body",
  "subject": "mail subject"
}`

# Configuration

Change the field paramenter in the handler, if your csv's 2nd field is not the email.