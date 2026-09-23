import json


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    question = body.get("question", "")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "question_received": question
        })
    }