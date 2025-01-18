import json
import boto3
import base64
import uuid
from urllib.parse import unquote_plus

# Initialize the S3 client
s3 = boto3.client('s3')

# Replace with your actual S3 bucket name
BUCKET_NAME = 'storepdffilebucket'

def lambda_handler(event, context):
    """
    Stores a base64-encoded file into an S3 bucket.

    Expected input format (JSON):
    {
        "file_name": "example.pdf",
        "file_content": "<base64-encoded string>"
    }

    Returns:
        JSON response with the S3 file URL.
    """
    try:
        # Parse the incoming event body
        body = json.loads(event.get('body', '{}'))
        file_name = body.get('file_name')
        file_content = body.get('file_content')

        # Validate presence of both file_name and file_content
        if not file_name or not file_content:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Both 'file_name' and 'file_content' are required."})
            }

        # Decode the base64 file content
        try:
            file_data = base64.b64decode(file_content)
        except base64.binascii.Error:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Invalid base64-encoded file content."})
            }

        # Generate a unique file name to prevent overwriting
        unique_file_name = f"{uuid.uuid4()}_{unquote_plus(file_name)}"

        # Upload the file to S3
        s3.put_object(Bucket=BUCKET_NAME, Key=unique_file_name, Body=file_data)

        # Construct the file URL
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{unique_file_name}"

        # Prepare the response
        response = {
            'statusCode': 200,
            'body': json.dumps({"file_url": file_url})
        }

        return response

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid JSON format."})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
