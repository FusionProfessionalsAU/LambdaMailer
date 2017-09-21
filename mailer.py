import boto3
import uuid

ses = boto3.client('ses')
s3_client = boto3.client('s3')

def send_anonymous_email(email_from, email_to, email_subject, email_body):
    ses.send_email(
        Source = email_from,
        Destination={
            'BccAddresses': email_to
        },
        Message={
            'Subject': {
                'Data': email_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        }
    )

def emails_from_s3(bucket, key, column):
    emails = []
    path = '/tmp/{}_{}'.format(uuid.uuid4(), key)
    s3_client.download_file(bucket, key, path)
    with open(path, "r") as f:
        for line in f:
            items = line.split(",")
            if len(items)>column:
                emails.append(items[column])
    return emails
    
    
def lambda_handler(event, context):
    send_anonymous_email(event['from'],emails_from_s3(event['bucket'], event['filename'], 1),event['subject'],event['body'])