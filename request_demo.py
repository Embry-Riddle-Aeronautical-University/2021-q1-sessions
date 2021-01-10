import requests

response = requests.get('https://api.github.com/users/wolfpaulus')

data = response.json() # magic .. converts text->json->dict all in a single line

print(type(data))
print(data)
print(data.get('followers'))
