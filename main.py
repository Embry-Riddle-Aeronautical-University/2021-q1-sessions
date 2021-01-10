import json
from math import sqrt

def is_prime(k: int) -> bool:
    """A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers"""
    if k < 2:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    for i in range(3, 1 + int(sqrt(k)), 2):
        if k % i == 0:
            return False
    return True

def lambda_handler(event, context):
    k = int(event["queryStringParameters"]["k"])
    b = is_prime(k)
    t = "is" if b else "is not"
    s = f'{k} {t} a prime number!'
    return {
        'statusCode': 200,
        'body': json.dumps(s)
    }
