import requests

r = requests.get(' https://newsapi.org/v2/top-headlines?country=us&apiKey=4502b5e1b10b488f99a4abc72f717a0b')
print(r.text)
print(r.status_code)

"""
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)
print(x.text)
print(x.status_code)
"""

url="http://dummy.restapiexample.com/api/v1/create"
data1={"name":"test1234","salary":"123","age":"23"}
x = requests.post(url=url, data = data1)
print(x.text)
print(x.status_code)
