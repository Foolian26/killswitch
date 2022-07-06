import requests

kill = requests.get('http://example.com/')#or a Pastebin Link

if kill.status_code == 200:
    pass
else:
    exit()

#Your Programm Here
print("Hello World")