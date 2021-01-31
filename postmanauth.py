import requests

url = "https://postman-echo.com/basic-auth"
headers = {
    "authorization": "Basic cG9zdG1hbjpwYXNzd29yZA==",
    "cache-control": "no-control"
}
response = requests.request("GET", url, headers=headers)

print(response.text)