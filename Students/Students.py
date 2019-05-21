import json
file = open('absolventi.json', encoding='utf-8')
text = file.read()
absolventi = json.loads(text)
print(absolventi)
print(len(absolventi))
####
import requests
import json
response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)
print(data)
print(len(data))
#for item in data:
for item in data[0]:
    print(item)
sumMale = 0
sumFemale = 0
for man in data:
    #print(man['gender'])
    if man['gender'] == 'Male':
        sumMale = sumMale + 1
    else:
        sumFemale = sumFemale + 1

print('Men:    ', sumMale)
print('Female: ', sumFemale)
####
response = requests.get('http://svatky.adresa.info/json')
#names = namefile.read()
names = json.loads(response.text)
print(names)
