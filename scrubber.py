import urllib.request
import urllib.parse
import re

url = 'https://www.youtube.com/watch?v=5GzVNi0oTxQ'
tokenisedUrl = re.search('(https:.*\/watch)(\?([A-Za-z])=([A-Za-z_0-9]*))', url).groups()
baseUrl = tokenisedUrl[0]
paramDef = tokenisedUrl[2]
paramVal = tokenisedUrl[3]

print('baseUrl '+baseUrl)
print('paramDef '+paramDef)
print('paramVal '+paramVal)

values = {paramDef:paramVal}
param = urllib.parse.urlencode(values)
param = param.encode('utf-8')
headers = {}
headers['User-Agent'] = 'Mozilla 5.10'
request = urllib.request.Request(baseUrl,param, headers=headers)
response = urllib.request.urlopen(request)
print(reponse.read())
