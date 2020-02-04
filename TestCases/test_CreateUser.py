import requests
import json
import jsonpath
import pytest

#API URL
url = "https://reqres.in/api/users"

def test_CreatUser():
    file = open('C:\\Users\\AVINASH\\PycharmProjects\\APIAutomation\\TestData\\CreateUser.json','r')
    json_input = file.read() #JSON Text
    request_json = json.loads(json_input) #Convertin JSON Text to JSON Object

    response = requests.post(url,request_json)
    print(response)
    assert response.status_code == 201
    #Parse the response to JSON Format
    response_json = json.loads(response.text)
    print(response_json)
    #Fetch the Key=ID value from the JSON Response
    id = jsonpath.jsonpath(response_json,'id')
    print(id)