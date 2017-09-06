import urllib, urllib2
import sys
import os
import requests
import urllib

opt1 = sys.argv[1]
appName = sys.argv[2]
opt2 = sys.argv[3]
appID = sys.argv[4]
opt3 = sys.argv[5]
token = sys.argv[6]

url = 'http://192.168.43.239:9090/api/scan_binary/'

path = appName

# file_name = appName
# urllib.urlretrieve(path,file_name)

files = {'binaryFile': open(path,'rb')}

values = {
		  'Uid' : appID,
           }

authtoken = "JWT "+str(token)

headers = { "Authorization" : authtoken }

response = requests.post(url, data=values,files=files,headers=headers)

print response.json()
