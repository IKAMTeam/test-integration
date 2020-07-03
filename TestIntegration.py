import OVIntegration
import json

with open('PasswordFile.json', "rb") as SFile:
    passwordData = json.loads(SFile.read().decode('utf-8'))

user = passwordData["UserName"]
password = passwordData["Password"]
site = passwordData["URL"]
trackorType = passwordData["TrackorType"]
trackorKey = passwordData["TrackorKey"]

with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

processId = ihub_data['processId']

integrationOV = OVIntegration.OVIntegration(url=site, userName=user, password=password, trackorType=trackorType, trackorKey=trackorKey, processId = processId)
