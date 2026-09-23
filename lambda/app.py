import json
import boto3

bedrock = boto3.client("bedrock-runtime")

MODEL_ID = "amazon.nova-micro-v1:0"


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    question = body.get("question", "")

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": question
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 300,
            "temperature": 0.3
        }
    )

    answer = response["output"]["message"]["content"][0]["text"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "answer": answer
        })
    }