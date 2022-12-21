import requests

githubUsername= "avirup171"
baseGetURL="https://api.github.com/users/"

apiUrl=baseGetURL+githubUsername
response = requests.get(apiUrl)
print(response)


responseBody=response.json()

print(responseBody["login"])
print(responseBody["name"])
print(responseBody["company"])
print(responseBody["bio"])
