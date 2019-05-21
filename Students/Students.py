import json
file = open('absolventi.json', encoding='utf-8')
text = file.read()
absolventi = json.loads(text)
print(absolventi)
####
import requests
import json
response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)
print(data)