import json
data='{ "var1":"Harry","var2":56}'
print(data)
# print(data['var1'])

prased=json.loads(data)
print(prased)
print(prased['var1'])
# print(type(prased))

data2={
    "chanel":"codewithharry",
    "cars":["BMW","audi a8","ferrari"],
    "fridge":("roti",560),
    "isbad":False
}
jscomp=json.dumps(data2)
print(jscomp)