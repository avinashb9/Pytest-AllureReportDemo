# Pytest-AllureReportDemo
Allure Report Integration with Pytest Framework of API testing

Used reqres.in public API for testing

Execution Steps:
Right click on the Project > Open in Terminal
Below command is to execute the test cases in TestCases directory
pytest -v -s --alluredir="C:\Users\AVINASH\PycharmProjects\APIAutomation\Reports" TestCases
open cmd--> navigate to Project/Reports path
execute below command to convert the Reports to Allure Reports
allure serve "C:\Users\AVINASH\PycharmProjects\APIAutomation\Reports"
