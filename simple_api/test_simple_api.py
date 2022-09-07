import requests

url = 'http://nutanix.selfhost.eu:5000/api/info'
myobj = {'battery_status': '30'}

x = requests.post(url, json= myobj)

print(x.text)