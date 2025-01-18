import json

# Lambda handler function 

def lambda_handler(event, context):
    """
    Adds two numbers provided in the event body and returns the result.

    Expected input format (JSON):
    {
        "number1": <int or float>,
        "number2": <int or float>
    }

    Returns:
        JSON response with the sum.
    """
    try:
        # Parse input from the event body
        body = json.loads(event.get('body', '{}'))
        number1 = body.get('number1')
        number2 = body.get('number2')

        # Validate that both numbers are present
        if number1 is None or number2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Both 'number1' and 'number2' are required."})
            }

        # Validate input types
        if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "'number1' and 'number2' must be integers or floats."})
            }

        # Calculate the sum
        result = number1 + number2

        # Prepare the response
        response = {
            'statusCode': 200,
            'body': json.dumps({"result": result})
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
