import urllib.request
import urllib.parse

url = 'https://www.youtube.com/watch'
values = {'v':'5GzVNi0oTxQ'}

data = urllib.parse.urlencode(values)
data.encode('utf-8')
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
responseData = reponse.read()
print(responseData)
