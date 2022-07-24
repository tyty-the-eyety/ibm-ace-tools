#!/usr/bin/python
import os
import requests
import sys

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
print (sys.argv[1])
print (sys.argv[2])

headers = {
    "Content-Type" :"text/xml",
    "Authorization": "Basic USER:USER_TOKEN"
}


appName = str(sys.argv[1]).replace(' ','')
gitName = str(sys.argv[2]).replace(' ','')
#print(x[0] , x[1])
with open('/var/lib/jenkins/jenkins_build_template.xml', 'r') as build_file :
    filedata = build_file.read()
    filedata = filedata.replace('[planName]', appName)
    filedata = filedata.replace('[gitRepo]', gitName)
    #with open(appName+'.xml', 'w') as file:
    #    file.write(filedata)
    r = requests.post('http://<hostname>:<port>/job/IIB-BUILD/createItem?name='+appName,data = filedata ,headers=headers)
    if r.status_code == 200:
        print(r.status_code)
        print ("Build plan " + appName + " created")
    else:
        print(r.status_code)
        print ("Build plan " + appName + " error")
        print(r.text)
with open('/var/lib/jenkins/jenkins_deploy_template.xml', 'r') as deploy_file :
    filedata = deploy_file.read()
    filedata = filedata.replace('[planName]', appName)
    filedata = filedata.replace('[gitRepo]', gitName)
    r = requests.post('http://<hostname>:<port>/job/IIB-DEV/createItem?name=DEV_'+appName,data = filedata ,headers=headers)
    if r.status_code == 200:
        print(r.status_code)
        print ("DEV_ plan " + appName + " created")
    else:
        print(r.status_code)
        print ("DEV_ plan " + appName + " error")
        print(r.text)
    r = requests.post('http://<hostname>:<port>/job/IIB-QA/createItem?name=QA_'+appName,data = filedata ,headers=headers)
    if r.status_code == 200:
        print(r.status_code)
        print ("QA_ plan " + appName + " created")
    else:
        print(r.status_code)
        print ("QA_ plan " + appName + " error")
        print(r.text)
    r = requests.post('http://<hostname>:<port>/job/IIB-PRE/createItem?name=PRE_'+appName,data = filedata ,headers=headers)
    if r.status_code == 200:
        print(r.status_code)
        print ("PRE_ plan " + appName + " created")
    else:
        print(r.status_code)
        print ("PRE_ plan " + appName + " error")
        print(r.text)
    r = requests.post('http://<hostname>:<port>/job/IIB-PROD1/createItem?name=PROD1_'+appName,data = filedata ,headers=headers)
    if r.status_code == 200:
        print(r.status_code)
        print ("XDE_ plan " + appName + " created")
    else:
        print(r.status_code)
        print ("XDE_ plan " + appName + " error")
        print(r.text)
    r = requests.post('http://<hostname>:<port>/job/IIB-PROD2/createItem?name=PROD2_'+appName,data = filedata ,headers=headers)
    if r.status_code == 200:
        print(r.status_code)
        print ("XZA_ plan " + appName + " created")
    else:
        print(r.status_code)
        print ("XZA_ plan " + appName + " error")
        print(r.text)

