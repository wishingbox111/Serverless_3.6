import boto3 #the boto3 is giving error cause there is no boto3 installed in the computer. When running on cloud it'll not give issues.
def lambda_handler(event, context):
    result = "Hello World"
    return {
        'statusCode' : 200,
        'body': result
    }