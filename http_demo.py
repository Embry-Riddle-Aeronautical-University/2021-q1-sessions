import requests
import json

# url = 'https://0q7qa8xj60.execute-api.us-west-2.amazonaws.com/Prod/synthesize'
#
# payload = {
#     "text": "What's going on today?",
#     "input_language": "en-US",
#     "output_language": "de-DE",
#     "synthesis": False,
#     "gender": "female"
# }
#
# response = requests.post(url=url, json=payload)
#
# d = response.json()
# print(type(d))
# print(d.get('translation'))


s = '{"key": "value","abc": f(range(10))}'

d = eval(s)
print(type(d))
print(d)
