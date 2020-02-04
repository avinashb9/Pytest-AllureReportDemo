import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"

file = open('C:\\Users\\AVINASH\\PycharmProjects\\APIAutomation\\TestData\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input) #Converting JSON Text to JSON Object

response = requests.put(url,request_json)
print(response)
response_json = json.loads(response.text)
print(response_json)
assert response.status_code == 200
