import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)

#Response Content
print(response.content)
print(response.headers)

#Fetch the Respnse as a JsonText
json_response = json.loads(response.text)
print(json_response)

#Fetch particular key from JSON
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages)